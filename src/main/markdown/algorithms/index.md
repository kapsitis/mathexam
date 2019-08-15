# DatZ4020: Lietišķie algoritmi

[Uz sākumu](../LU/index.html) > **DatZ4020**

* [Kursa apraksts (LU kursu katalogs)](https://www.lu.lv/lv/nc/studijas/studiju-celvedis/programmu-un-kursu-katalogi/kursu-katalogs/?tx_lustudycatalogue_pi1%5Bcourse%5D=DatZ4020&tx_lustudycatalogue_pi1%5Baction%5D=detail&tx_lustudycatalogue_pi1%5Bcontroller%5D=Course&cHash=c3ba047ba1e7775b94f0d291e49368ef)
* [Guy Blellock kursa mājaslapa (Carnegie Mellon)](http://www.cs.cmu.edu/~guyb/rwc/)
* [Syllabus](syllabus.html)

## Kursa mērķi 

Kursa ietvaros dalībnieki mācās analizēt dažādus netriviālus algoritmus, kuri turklāt bieži parādās programmēšanas
ikdienā un sadzīvē (attēlu un citu mediju formāti, informācijas pārraidīšana un šifrēšana, lineārā optimizācija, Google meklētāja
Page Rank algoritms, dažādi virkņu meklēšanas algoritmi). 

## Kursa sagatavošana

* [Materiāla veidošanas process](isd-process.html) - aprakstīti daži kursa analīzes un gatavošanas soļi un pielinkoti to rezultāti, piemēram, analīzes dokumenti.
* **[Prasmju analīze (task analysis)](task-analysis.html)** - šī ir svarīgākā un darbietilpīgākā kursa analīzes daļa; atbildam uz jautājumiem, kas dalībniekiem būtu jāprot, 
kursu beidzot. 

## Kursa plāns

Katras teorijas tēmas beigās pievienojam "pasaku" - apmēram 10 minūšu stāstījumu par kādu algoritmu lietojuma aspektu ar ārējām norādēm 
tiem, kuri grib uzzināt kaut ko vairāk. 

1. Informācijas teorijas jēdzieni, entropija. Hofmana saspiešana.  
*Pasaka:* Kādas atvērtā koda vai brīvprogrammatūras implementācijas ir pieejamas šī kursa algoritmiem - pārskats.
Kādos gadījumos Jums palīdz algoritma izpratne, spēja pašiem kodēt par līdzīgām tēmām.
2. **Datu bezzudumu saspiešanas jēdzieni.** Vispārīgā prefiksu saspiešana un prefiksu koki. Aritmētiskā saspiešana.   
*Pasaka:* Empīriska saspiešanas mērīšana (biti uz simbolu). Entropija un saspiešanas teorētiskā robeža. Saspiežamības atkarība no valodas un failu žanra. Kalgari korpuss. 
3. Bezzudumu saspiešana, LZ77 un Lempela-Ziva-Velča algoritmi.  
*Pasaka:* LZW un GIF - kas ir "patentēti" algoritmi un failu formāti, vārda brīvība algoritmu pasaulē.
4. Berouza-Vīlera algoritms.  
*Pasaka:* Arhivēšanas rīku gz/WinZIP, gzip2 u.c. pārskats. Kas ir PNG saspiešanas līmenis (*compression level*). 
HTTP sūtāmo failu un biroja programmu formātu (**docx**, nevis **doc**) saspiešanas sekas.
5. **Datu zudumradošā saspiešana - 1**. Diskrētais kosinusu pārveidojums, JPEG algoritms.  
*Pasaka:* Krāsu kodēšana, acīm atšķiramas atšķirības, Raw un JPEG dati foto un video aparatūrā. 
6. Datu zudumradošās saspiešana - 2. Solomona-Rīda algoritms.  
*Pasaka:* MP3 un daži video formāti, to DRM (*digital rights management*). Redzamās un neredzamās ūdenszīmes mediju failos 
(*watermarking algorithms*); to robustums atkarībā no saspiešanas veida.
7. **Kļūdu korekcijas algoritmi - 1.** Heminga kods, piemēri un vispārīgais gadījums. Rīda-Solomona kodi.  
*Pasaka:* Steganogrāfija jeb informācijas "paslēpšana" ar to nesaistītā failā. Izaicinājumi tiem, 
kuri vēlas aizsargāt uzņēmumus un iestādes pret konfidenciālu datu noplūdēm: Data Leak Prevention (DLP).
8. Kļūdu korekcijas algoritmi - 2. Galīgu lauku jēdziens. Grafu kodi un Tornado kodi.
*Pasaka:* TCP/IP saimes tīklošanās protokoli, kuros izmanto redundanci. <span style="color:red">Semestra vidus eksāmens</span> (*Midterm exam*). 
9. **Lineārā programmēšana - 1.** Optimizācijas problēmu veidi. Lineārās programmēšanas vizualizācija zemām dimensijām. Simpleksalgoritma ievads.  
*Pasaka:* Transporta, preču ražošanas u.c. uzdevumi, kas noved pie lineārās optimizācijas.
10. Lineārā programmēšana - 2. Simpleksu algoritms, tā korektums. Primārā un duālā lineārā programma.  
*Pasaka:* Algoritmu sarežģītība (laika un telpas prasības aprēķina veikšanai atkarībā no ievades datu lieluma); 
praksē populāri algoritmi, kam ir slikti "sliktākie gadījumi". 
11. Lineārā programmēšana - 3. Elipsoīda algoritms. Iekšējā punkta metode un tās varianti (afīnā mērogošana, potenciāla redukcija, centrālā trajektorija).  
*Pasaka:* Lineāri modeļi Google meklēšanas rezultātu ranžējumā (*Page Rank*), Netflix rekomendācijās utml. 
12. **Meklēšana virknēs.** Algoritmisko problēmu definīcijas. Naivais algoritms. Knuta-Morisa-Prata algoritms, tam veidojamās
datu struktūras (tabuliņas). Laika sarežģītības salīdzinājums.  
*Pasaka:* Vienkāršs zināšanu pārvaldības (*knowledge management*) uzdevums - kā nepazaudēt pašam savus dokumentus. 
Teksta dokumentu indeksācijas rīku salīdzinājums un to ātrdarbība.
13. Meklēšana virknēs - 2. Bojera-Mūra algoritms. Laika sarežģītības salīdzinājums ar KMP.   
*Pasaka:* Antivīrusu skenēšana, tradicionālās AV produktu *vīrusu signatūras*. Kā iepakot vīrusus, lai no tām izvairītos.
14. Meklēšana virknēs - 3. Dinamiskā programmēšana. Ukkonena algoritms. Edsgera Deikstras (*Edsger W. Dijkstra*) algoritms. 
*Pasaka:* Regulāru izteiksmju meklēšanas lietojumi DLP produktos (kā pasargāt organizācijas datortīklu no cilvēku vārdu, adresu, telefonu u.c. 
noplūdes). Kā rakstīt regulāras izteiksmes, lai DLP skenēšana būtu efektīva. Kāpēc kredītkaršu datu noplūdes parasti 
nemeklē ar regulārām izteiksmēm. 
15. Pārskata nodarbība. <span style="color:red">Gala eksāmens</span> (*Final exam*). 



