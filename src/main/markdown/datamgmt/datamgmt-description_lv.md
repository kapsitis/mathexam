# Kurss: Datu pārvaldības un analīzes ietvari

## Vispārīga informācija par piedāvājumu 

(*Šī ir kursa apraksta skice*) 

* **Fakultāte:** Datorikas fakultāte
* **Auditorijas stundu skaits:** 32-64 (2 vai 4cr)
* **Lekciju stundu skaits:** 32-64
* **Patstāvīgā darba stundu skaits:** 32 


**Kursa anotācija:** Starpdisciplinārā nozare, ko bieži 
sauc par "Datu mācību" (*Data science*) dažādi atspoguļojas
akadēmiskajā izglītībā. Ir kursi par datu struktūrām programmēšanā, 
par relāciju (hierarhiskajām u.c.) datubāzu vadības sistēmām, 
par statistiku, par datu analīzi un vizualizāciju, par ontoloģijām, 
metadatu pievienošanu un inferenci, par mašīnmācīšanos no datiem, 
par valodas tekstu apstrādes rīkiem, kā arī datu noliktavām, datizraci 
un *Business Intelligence*.  
Minētās nozares izmanto pietiekami standartizētu tehnoloģiju kopumu 
(*data management stacks*) un lielu IT sistēmu veidošanai 
piemērotus arhitektūras principus, kas nodrošina sistēmas integrēšanu 
ar datu avotiem reālā laikā, apraksta publicējamo datu 
modeli un pārbauda aktuālo datu validitāti. Turpmāk šī infrastruktūra
atbalsta gan strukturētu (pa stingru datutipu kolonnām sadalītu), gan 
nestrukturētu (brīva teksta) datu meklēšanu un analīzi, 
atbalsta noteikta veida biznesa loģiku un pārskatu ģenerēšanu kā arī 
veco datu izdzēšanu (*burn-off*). 

**Rezultāti:** 

1. Pēc šī kursa apgūšanas dalībniekiem ir prasme darboties
ar minimālistiskām (bet visus būtiskos aspektus iekļaujošām)
datu pārvaldības infrastruktūrām (*stacks*), nodrošinot 
stekā ietilpstošo rīku integrāciju ar RESTful (t.i. JSON-balstītām)
saskarnēm.
2. Kursa dalībniekiem ir pieredze lietot NiFi un Kafka ietvarus
datu publicēšanai, ElasticSearch vai Hadoop serverus to glabāšanai, 
Elastic, Logstash, Kibana (ELK) ietvaru strukturētu (piemēram, žurnālfailu)
datu apstrādei, Apache Lucene ietvaru pilna teksta meklēšanai. 
3. Kursa dalībnieki veido vienkāršas datos balstītas lietojumprogrammas, 
piemēram, analizējot Twitter ierakstus vai sensoru datus reālā laikā.


## Kursa plāns

1. Atkārtojums par strukturēto datu tipiem. Veseli un reāli skaitļi, datumi, 
stringi/virknes, klasifikatori. Unikāli identifikatori un norādes
(jeb primārās un ārējās atslēgas). Strukturēti datu tipi
vaicājumu valodās (SQL, SPARQL, Elastic).
2. Nestrukturēti dati. Tekstu kodējumi, vārdu celmošana (*stemming*), 
indeksu veidošana. Lucene vaicājumu sintakse. 
3. SQL un NoSQL datubāzes: PostgreSQL, MongoDB un Elastic 
salīdzinājums. 
4. RESTful interfeisi/saskarnes datu piegādātāju un patērētāju savstarpējai 
integrēšanai. 
5. Datu publicēšanas slānis: NiFi (Niagara Files) un Kafka. 
6. Ziņojumu rindu slānis: RabbitMQ, publicētāja-abonenta modelis. 
7. Žurnalēšanas un monitorēšanas slānis: Kibana, Grafana.
8. Pieprasījumu būvēšanas slānis: Domēnspecifisku pieprasījumu pārveidošana
par zema līmeņa datu pieprasījumiem. 
9. Nepārtrauktās integrācijas un DevOps automatizācijas slānis: 
Jenkins, Docker un Ansible. 
10. Datu pārvaldības infrastruktūru lietojumi - mašīnmācīšanās, 
"digital humanities", UEBA (User and Entity Behavioral Analytics), 
citi reāla laika vai pakešu (*batch*) datu integrēšanas un analīzes
uzdevumi.


