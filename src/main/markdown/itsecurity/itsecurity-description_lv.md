# Kurss: IT drošības un datu aizsardzības principi

[Uz sākumu](http://85.254.250.28/learning/LU/)

## Vispārīga informācija

(*Šī ir kursa apraksta skice*) 

* **Fakultāte:** Datorikas fakultāte
* **Auditorijas stundu skaits:** 32 vai 64
* **Lekciju stundu skaits:** 32
* **Patstāvīgā darba stundu skaits:** (Var būt daudzveidīgi praktiskie darbi).

**Kursa anotācija:** Uzņēmumu un organizāciju IT un datu drošību var veicināt, ievērojot 
noteiktas procedūras, ieviešot drošības arhitektūras (piemēram, pareizi izveidotu 
PKI infrastruktūru vai 2-faktoru autentifikāciju) un arī lietojot īpašus rīkus. 
Pēdējo gadu laikā daudzi uzņēmumiem kritiski dati ir pācēlušies uz t.s. *mākoņiem* - 
citu uzņēmumu (vai pat citu valstu) kontrolē esošiem serveriem. Tādēļ izmainījies
arī priekšstats par drošības riskiem - mazāks uzsvars uz perimetra aizsardzību, ko nodrošina
politikas (*policy rules*), kas ierakstītas ugunsmūros vai 
Web/Email vārtejās (*gateways*).  
Mūsdienās lielāka uzmanība 
ir lietotāju uzvedības novērošanai, noteikta veida anomāliju pazīšanai, izmantojot informāciju, kas 
savākta tradicionālajās tīkla perimetra ierīcēs un arī specializētos programmatūras aģentos 
(*endpoint agents*) un arī lietojot mašīnmācīšanās pieejas, uzvedības paraugu pazīšanai.
Lai drošības arhitektūru un rīku lietotājs (piemēram, IT palīdzības dienesta darbinieks, 
datu drošības inženieris, lielas informācijas sistēmas arhitekts u.c.) varētu pareizi 
integrēties ar esošiem drošības rīkiem, viņam/viņai nepieciešamas zināšanas par vispārīgiem principiem, 
kuri ir ļoti daudzu uzņēmumu drošības risinājumu un rīku pamatā. 

## Rezultāti

1. Kursa dalībnieki atšķir drošības/uzbrukumu kanālus (tīklu protokoli, 
darbības lietotāju darbstacijās, failu glabātuves) un saprot to aizsardzībai nepieciešamo 
pieeju atšķirības.
2. Kursa dalībnieki orientējas datortīklu topoloģijā, izmanto vienkāršas komutatoru (*switch*) un
maršrutētāju (*routers*) konfigurācijas, konfigurē NAT un portu pāradresāciju. 
3. Kursa dalībnieki konfigurē atvērta izejas koda Web starpniekserverus (Squid), pārtver ar
tiem HTTPS protokolu, piesaista starpniekserverim papildus pieprasījumu/atbilžu 
analīzes moduļus, izmantojot ICAP. 
4. Kursa dalībnieki saprot PKI infrastruktūru, elektroniskos parakstus, TLS sertifikātu 
ieteicamo struktūru mazos/vidējos uzņēmumos un valsts iestādēs, šo sertifikātu derīguma problēmas.
5. Kursa dalībnieki prot konfigurēt Epasta vārtejas, šifrēt epastus līdz saņēmēja serverim ar 
TLS sertifikātu kā arī līdz galasaņēmējam (piemēram ar PGP). 
6. Kursa dalībnieki pārzina deleģētās autentifikācijas pieejas, kā lieli uzņēmumi 
nodrošina vienreizēju paroles ievadi (*single sign-on*), lai pieslēgtos dažādiem resursiem, t.sk. 
arī mākonī. Kursa dalībnieki prot izmantot 2-faktoru autentifikāciju, piemēram, paroli kopā
ar telefona aplikāciju.
7. Kursa dalībnieki prot analizēt žurnālfailus, piemēram, izmantojot SIEM rīku Splunk, ierakstot
tajā savus datus ar syslog protokolu.
8. Kursa dalībnieki pārzina lietotāju risku un uzvedības analīzes (UEBA) rīku pamatiepējas, 
konfigurē tās, piemēram, izmantojot teksta meklēšanas iespējas žurnālfailos.

## Kursa plāns

1. Pārskats par drošības apdraudējumiem, motivāciju, kādēļ uzņēmumi iegulda šādās tehnoloģijās. 
Datu noplūdes, privātuma aizsardzība (GDPR), reputācijas un tiesāšanās riski, kritiskas infrastruktūras
apdraudējuma riski, darba laika izšķērdēšanas riski.
2. TCP/IP tīklošanās, tīklu topoloģijas un iptables. Vienkāršu ierobežojošu likumu konfigurēšana.
Minimāla aizsardzība, uzstādot savus serverus mākonī.
3. Bezvadu tīkli un to drošības riski. Ierīču autentifikācija bezvadu tīklos. 
VPN konfigurēšana. Ugunsmūru ierobežojumu apiešana ar VPN un SSH tuneļiem. 
4. Web protokoli (HTTP un HTTPS). Ar Web saistītie un caur to tunelētie citi pakalpojumi 
(versiju kontroles rīki, čats). Autentifikācijas pamatveidi HTTP-veida protokolos - *Basic*, *NTLM* un *Kerberos*. 
Autentifikācijas veidu noturība pret uzbrukumiem (protokolu noklausīšanās, *replay attacks*, 
*keyloggers*). 
5. SSL/TLS slānis HTTP un citu "atvērtu" protokolu šifrēšanai. PKI (publisko/privātu atslēgu 
infrastruktūra). Uzņēmuma "saknes sertifikācijas autoritāte", subordinētās autoritātes, 
to izsniegtās atslēgas. 
6. Web starpniekserveri (*Web proxies*), to drošības risinājumi. Satura filtrēšana, t.sk. "vecāku filtri"
vai filtri atbilstoši satura klasterizētajai kategorijai. Starpniekserveru iespējas pārtvert 
SSL protokolu.
7. Epasta un pļāpāšanas lietotņu drošības izaicinājumi. Paroļu un citas informācijas izvilināšana, atsūtot 
viltus linkus (*phishing*). NDR un *backscatter* uzbrukumi epastā. Epasta sūtītāja viltošana 
mēstuļu sūtīšanas risinājumos un to apkarošana (*reverse DNS lookup*, DKIM paraksti). 
8. Epasta protokolu (SMTP) drošības problēmas un to risinājumi: šifrēšana ar galasaņēmēja atslēgu. 
9. Deleģētā autentifikācija, 2-faktoru autentifikācija. 
10. SIEM un UEBA rīki - to konfigurācija un lietošana.



