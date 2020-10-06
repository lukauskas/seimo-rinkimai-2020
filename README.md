# Seimo rinkimai 2020, Manobalsas.lt duomenų analizė

Spalio vienuoliktoji, rinkimų diena jau ne už kalnų. Kalbančios galvos ragina visus keliauti balsuoti, bet [Delfi apklausa rugsėjo 30-ąją](https://www.delfi.lt/news/daily/lithuania/apklausa-pries-pat-seimo-rinkimus-reitingu-lenteleje-inirtinga-kova.d?id=85365653) raportuoja jog 15.8% apklaustųjų dar nėra apsisprendę už ką.

Neapsisprendėliams, [manobalsas.lt](https://www.manobalsas.lt/index/index.php) sukūrė testą su 33 klausimais apie šių dienų politines aktualijas apie kurias nuomonę galima išreikšti šešiais lygmenimis: *visiškai sutinku*, *greičiau sutinku*, *nei taip arba ne*, *nesutinku*, *visiškai nesutinku* ir - *neturiu nuomonės*. Šį testą manobalsas.lt portale atliko ir 318 politikų kandidatuojančių į jų seimą.

Šioje repozitorijoje mes žiūrime į jų atsakymus.

Duomenys priklauso manobalsas.lt. Jais nesidalijame čia.

Analizė mano. Analizė subjektyvi. Analizės grafikai/tekstas: [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/). 

## Duomenys

Duomenys gali būti parsisiųsti naudojant `data/download.py` skiptą.
Analizės kodas direktorijoj `notebooks`.

## Analizė

### Lengvi klausimai

Pirmiausia, kokiomis temomis mūsų politikai sutaria?

![`klausimai-pagal-nesutarima-top10.png`](notebooks/output/klausimai-pagal-sutarima-top10.png)

Absoliuti dauguma nepritaria sankcijų Rusijai švelninimui, išskyrus Centro partijos – tautininkus: Alfonsas Lupeikis (Visiškai sutinku), Daiva Kazakevičiūtė (Greičiau sutinku), Nerijus Meškauskas (Greičiau sutinku); Lietuvos socialdemokratų partijos narį: Valentin Gavrilov (Greičiau sutinku); Lietuvos liaudies partijos narį: Darius Gruzdys (Visiškai sutinku); Laisvės partijos narį: Algis Bitautas (Greičiau sutinku); Krikščionių sąjungos narį: Gediminas Akelaitis (Greičiau sutinku)

Taip pat politikai pritaria savivaldos skatinimui, ES palaikymui (lyginant su JAV), žmogaus teisių šalininakms Kinijoje, pilietybės išsaugojimui NATO/ES nariams, ir aplinkosaugos mokesčių didinimui. Politikai nepritaria laisvių suvaržymams kovojant su pandemija, bendradarbiavimui su Baltarusija žmogaus teisių kaina ir Astravo elektrinei. Taip pat politikai sutartinai atsako "nei taip nei ne" nusikaltėlių bausmės griežtinimo klausimu.

### Klausimai dalijantys politikus

![`klausimai-pagal-sutarima-top10.png`](notebooks/output/klausimai-pagal-nesutarima-top10.png)

Trys dalykai dalijantys lietuvos politiką labiausiai yra:

1. Asmenvardžių rašybą su `w`, 
2. Homoseksualių porų santuokos,
3. Lukiškių aikštė.

Ketvirtoje vietoje yra diskusijos apie pajamų mokestį, penktoje - marihuanos legalizacija (nors didžioji dalis yra prieš), po to: investicijos į valstybės gynybą, rinkos laisvė, proporcinė demokratija, laisva rinka sveikatos sistemoje, mokyklų tinklo mažinimas.

Tos pačios lyties santuokų klausimas dalijasi pagal partijų liberalizmo savivoką 
Laisvės partija ir Liberalų Sąjūdis yra viršuje, konservatoriškų pažiūrų partijos apačioje.

![`klausimas-11.png`](notebooks/output/klausimas-11.png)

Panašu, jog socialdemokratai yra pozityvūs šia tema, taip pat Lietuvos žalieji (ne valstiečiai!), o TS-LKD ir valstiečiai priešinasi.
Įdomu, jog tarp visų partijų yra gana didelė dalis maištautojų:

#### Liberalai ir socdemai kurie nepalaiko tos pačios lyties asmenų santuokų:

**LRLS**: Benediktas Krasniauskas (Nei taip, nei ne), Dalius Dirsė (Nei taip, nei ne), Kęstutis Bagdanavičius (Greičiau nesutinku), Mindaugas Sargūnas (Visiškai nesutinku), Nijolė Makštutienė (Nei taip, nei ne), Ričardas Leckas (Nei taip, nei ne),  Saulius Budinas (Greičiau nesutinku), Saulius Liekis (Nei taip, nei ne); **LP**:  Gražvyda Petrikaitė (Nei taip, nei ne), Jurgita Jokūbaitytė (Nei taip, nei ne), Vida Navickienė (Greičiau nesutinku)

Petrikaitė ir Krasniauskas komentuoja jog remtų idėjas tobulinti partnerystės įstatymus bet ne santuokas.

**Socdemai**:     Alfonsas Brazas (Nei taip, nei ne), Algirdas Sysas (Greičiau sutinku), Arūnas Dudėnas (Greičiau nesutinku), Dainius Žiogelis (Visiškai nesutinku), Daiva Riklienė (Greičiau nesutinku), Kęstutis Jacunskas (Greičiau nesutinku), Kęstutis Vilkauskas (Visiškai nesutinku), Lina Maižiuvienė (Greičiau sutinku), Ramūnas Lydis (Greičiau sutinku), Saulius Sondeckis (Greičiau nesutinku), Tomas Budrikis (Greičiau nesutinku), Tomas Martinaitis (Nei taip, nei ne), Valentin Gavrilov (Greičiau nesutinku), Vidmantas Kanopa (Greičiau nesutinku)

Brazas, Riklienė, Gavrilov pabrėžia jog palaiko partnerystes, ne santuokas

#### Konservatoriai ir valstiečiai kurie palaiko tos pačios lyties asmenų santuokas

**Konservatoriai**, kurie palaiko šias santuokas: Aistė Gedvilienė (Greičiau sutinku), Birutė Kažemėkaitė (Greičiau sutinku), Dalius Krinickas (Visiškai sutinku), Jurgita Sejonienė (Greičiau sutinku), Justinas Pranys (Greičiau sutinku), Kristijonas Bartoševičius (Greičiau sutinku), Kęstutis Navickas (Greičiau sutinku),  Matas Maldeikis (Visiškai sutinku), Paulė Kuzmickienė (Greičiau sutinku),  Radvilė Morkūnaitė-Mikulėnienė (Greičiau sutinku), Skaidra Dišlė (Visiškai sutinku)
    
**Lietuvos valstiečių ir žaliųjų sąjunga**: Agnė Prušinskaitė (Greičiau sutinku), Aušra Papirtienė (Greičiau sutinku), Liutauras Vičkačka (Greičiau sutinku), Martynas Norbutas (Visiškai sutinku), Tautvydas Tamulevičius (Visiškai sutinku), Tomas Tomilinas (Greičiau sutinku)

Dalius Krinickas komentaru pabrėžia jog gerbia visas žmogaus teises, o Gedvilienė, Sejonienė, Tomilinas komentuoja jog pritaria tik partnerystei. 

Įdomu, jog liberalai laiko partnerystės palaikymą "neigiamu" atsakymu, o kiti - teigiamu.


### Klausimai dalijantys partijas

#### Valstiečiai

![klausimai-pagal-nesutarima-Lietuvos-valstiečių-ir-žaliųjų-sąjunga.png](notebooks/output/klausimai-pagal-nesutarima-Lietuvos-valstiečių-ir-žaliųjų-sąjunga.png)

### TS-LKD

![klausimai-pagal-nesutarima-Tėvynės-sąjunga---Lietuvos-krikščionys-demokratai.png](notebooks/output/klausimai-pagal-nesutarima-Tėvynės-sąjunga---Lietuvos-krikščionys-demokratai.png)

### Socdemai

![klausimai-pagal-nesutarima-Lietuvos-socialdemokratų-partija.png](notebooks/output/klausimai-pagal-nesutarima-Lietuvos-socialdemokratų-partija.png)

### Liberalai

![klausimai-pagal-nesutarima-Lietuvos-Respublikos-liberalų-sąjūdis.png](notebooks/output/klausimai-pagal-nesutarima-Lietuvos-Respublikos-liberalų-sąjūdis.png)

### Laisvės partija

![klausimai-pagal-nesutarima-Laisvės-partija.png](notebooks/output/klausimai-pagal-nesutarima-Laisvės-partija.png)

## Bendra vizualizacija visų atsakymų į klausimus

![notebooks/output/visu-partiju-balsai.png](notebooks/output/visu-partiju-balsai.png)

## Detali vizualizacija atsakymų į kiekvieną klausimą

![notebooks/output/klausimas-1.png](notebooks/output/klausimas-1.png)

![notebooks/output/klausimas-2.png](notebooks/output/klausimas-2.png)

![notebooks/output/klausimas-3.png](notebooks/output/klausimas-3.png)

![notebooks/output/klausimas-4.png](notebooks/output/klausimas-4.png)

![notebooks/output/klausimas-5.png](notebooks/output/klausimas-5.png)

![notebooks/output/klausimas-6.png](notebooks/output/klausimas-6.png)

![notebooks/output/klausimas-7.png](notebooks/output/klausimas-7.png)

![notebooks/output/klausimas-8.png](notebooks/output/klausimas-8.png)

![notebooks/output/klausimas-9.png](notebooks/output/klausimas-9.png)
![notebooks/output/klausimas-10.png](notebooks/output/klausimas-10.png)
![notebooks/output/klausimas-11.png](notebooks/output/klausimas-11.png)
![notebooks/output/klausimas-12.png](notebooks/output/klausimas-12.png)
![notebooks/output/klausimas-13.png](notebooks/output/klausimas-13.png)
![notebooks/output/klausimas-14.png](notebooks/output/klausimas-14.png)
![notebooks/output/klausimas-15.png](notebooks/output/klausimas-15.png)
![notebooks/output/klausimas-16.png](notebooks/output/klausimas-16.png)
![notebooks/output/klausimas-17.png](notebooks/output/klausimas-17.png)
![notebooks/output/klausimas-18.png](notebooks/output/klausimas-18.png)
![notebooks/output/klausimas-19.png](notebooks/output/klausimas-19.png)
![notebooks/output/klausimas-20.png](notebooks/output/klausimas-20.png)
![notebooks/output/klausimas-21.png](notebooks/output/klausimas-21.png)
![notebooks/output/klausimas-22.png](notebooks/output/klausimas-22.png)
![notebooks/output/klausimas-23.png](notebooks/output/klausimas-23.png)
![notebooks/output/klausimas-24.png](notebooks/output/klausimas-24.png)
![notebooks/output/klausimas-25.png](notebooks/output/klausimas-25.png)
![notebooks/output/klausimas-26.png](notebooks/output/klausimas-26.png)
![notebooks/output/klausimas-27.png](notebooks/output/klausimas-27.png)
![notebooks/output/klausimas-28.png](notebooks/output/klausimas-28.png)
![notebooks/output/klausimas-29.png](notebooks/output/klausimas-29.png)
![notebooks/output/klausimas-30.png](notebooks/output/klausimas-30.png)
![notebooks/output/klausimas-31.png](notebooks/output/klausimas-31.png)
![notebooks/output/klausimas-32.png](notebooks/output/klausimas-32.png)
![notebooks/output/klausimas-33.png](notebooks/output/klausimas-33.png)


