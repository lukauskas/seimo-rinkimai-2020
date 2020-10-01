import requests
from lxml import etree
import pandas as pd
import re
from itertools import zip_longest
from ratelimit import limits, sleep_and_retry
from tqdm import tqdm

# Limit to 1 request per second
NUMBER_OF_REQUESTS = 1
PER_TIMEFRAME = 1 # Seconds

BASE_URL = 'https://www.manobalsas.lt'
URL_POLITIKAI = BASE_URL + '/politikai/politikai.php'

URL_TEMPLATE_TEST =  BASE_URL + '/politikai/atsakymu_lentele.php?pol_id={member_id}&tst={test_id}&all={all}'

@sleep_and_retry
@limits(calls=NUMBER_OF_REQUESTS, period=PER_TIMEFRAME)
def download_politikai():

    response = requests.get(URL_POLITIKAI)
    response.raise_for_status()

    response.encoding = 'utf-8'

    html = etree.HTML(response.text)
    div_politikai = html.xpath('//div[@id="politikai"]')[0]

    div_parties = div_politikai.xpath('.//div[contains(@class, "party")]')

    answer = []

    for div_party in div_parties:
        party_name = div_party.xpath('./h2/text()')[0].strip(' -')
        member_anchors = div_party.xpath('./div/ul/li/a')

        for anchor in member_anchors:

            member_href = anchor.xpath('./@href')[0]
            assert member_href.startswith('../')
            member_url = BASE_URL + member_href[2:]


            member_name = anchor.xpath('./text()')[0].strip('')

            answer.append([party_name, member_url, member_name])


    answer = pd.DataFrame(answer, columns=['party', 'member_url', 'member_name'])

    return answer

@sleep_and_retry
@limits(calls=NUMBER_OF_REQUESTS, period=PER_TIMEFRAME)
def get_member_id(party_member_url):

    response = requests.get(party_member_url)
    response.raise_for_status()
    response.encoding = 'utf-8'

    html = etree.HTML(response.text)

    show_more_href = html.xpath('//a[contains(@href, "parodyti_visus_atsakymus")]/@href')[0]

    match = re.match(
        'javascript:parodyti_visus_atsakymus\((?P<member_id>\d+),\s*(?P<test_id>\d+),\s*(?P<all>\d+)\);',
        show_more_href
    )

    member_id = int(match.group('member_id'))
    test_id = int(match.group('test_id'))
    all_ = int(match.group('all'))

    return member_id, test_id, all_


# From itertools recipes
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

@sleep_and_retry
@limits(calls=NUMBER_OF_REQUESTS, period=PER_TIMEFRAME)
def get_member_answers(member_id, test_id, all_):

    url = URL_TEMPLATE_TEST.format(member_id=member_id, test_id=test_id, all=all_)
    response = requests.get(url)

    response.raise_for_status()
    response.encoding = 'utf-8'

    html = etree.HTML(response.text)


    question_tables = html.xpath('//table/tbody')

    df = []

    for question_table in question_tables:

        question_table_tds = question_table.xpath('./td')

        # For some reason they do not return TRs so we
        # need to iterate trough TDs eight at a time
        for row in grouper(question_table_tds, 8):

            question = ' '.join(row[0].xpath('./text()')).strip()
            answers = [len(c.xpath('./img[contains(@src, "politikas")]')) > 0 for c in row[1:7]]
            assert sum(answers) == 1

            true_answer = answers.index(True)
            answer_order = ['Visiškai sutinku', 'Greičiau sutinku', 'Nei taip, nei ne', 'Greičiau nesutinku', 'Visiškai nesutinku', 'Neturiu nuomonės']
            answer = answer_order[true_answer]

            comment = ' '.join(row[7].xpath('./text()')).strip()

            df.append([question, answer, comment])

    df = pd.DataFrame(df, columns=['question', 'answer', 'comment'])

    return df


def get_all():

    politikai = download_politikai()

    ans = []

    for __, row in tqdm(politikai.iterrows(), total=len(politikai)):
        party_name = row['party']
        member_url = row['member_url']
        member_name = row['member_name']

        member_id = get_member_id(member_url)
        answers = get_member_answers(*member_id)

        answers['party'] = party_name
        answers['member_name'] = member_name

        ans.append(answers)

    ans = pd.concat(ans, ignore_index=True)
    ans = ans[['party', 'member_name', 'question', 'answer', 'comment']]

    return ans

if __name__ == '__main__':
    ans = get_all()
    ans.to_csv('data.tsv', sep='\t', index=False)
