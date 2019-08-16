# DatZ4020: Prasmju analīze

[LU kursi](../LU/index.html) > [DatZ4020](index.html) > **Prasmju analīze**

1. Lietot un analizēt bezzudumu saspiešanas algoritmus
    1. Formulēt un lietot vispārīgus jēdzienus par saspiešanas algoritmiem.
        1. Definēt alfabētu, vārdus un valodas.  
*Pārbaude:* Dots konteksts; jāatrod, kas tajā ir "alfabēti", "vārdi" un "valodas".
        2. Saskaitīt noteikta garuma virknes dotajā alfabētā (ar vai bez papildu ierobežojumiem).  
*Pārbaude:* Alfabēta burtu skaitam, virknes garumam vai intervālam (plus dažiem fiksētiem burtiem virknē vai citiem ierobežojumiem) noteikt iespējamo virkņu skaitu.
        3. Definēt entropiju ar burtu vai citu teksta gabaliņu biežuma varbūtībām; aprēķināt to nelielam burtu skaitam.  
*Pārbaude:* Dotajām burtu varbūtībām aprēķināt entropiju. Saprast, kā mainās entropija, ja burtu varbūtības kļūst vienādas/ļoti dažādas, ja burtus grupē pa vairākiem kopā utml.
        4. Definēt (bezzudumu) saspiešanas funkciju un tai inverso.   
*Pārbaude:* Aprakstīt funkcijas definīcijas un vērtību apgabalus, raksturot entropiju algoritma ieejā un izejā. Pēc konteksta noteikt, ar ko datu saspiešana līdzinās vai atšķiras no šifrēšanas.
        5. Pierādīt universāla saspiešanas algoritma neesamību.   
*Pārbaude:* Atjaunot pierādījumus (ar Dirihlē principu un variantu saskaitīšanu) par tēmu, ka jebkāds saspiešanas algoritms vairumu ievades datu nevis saspiež, bet pat nedaudz palielina. 
    2. Aprakstīt un pamatot apgalvojumus par prefiksu saspiešanu
        1. Aprakstīt Hofmana saspiešanas metodi.
        2. Konstruēt prefiksu kokus, zinot burtu parādīšanās varbūtības. 
        3. Pamatot atkodēšanas viennozīmīgumu, ja kodēšanai izmantots prefiksu koks (neviens kods nav otram prefikss).
        4. Aprakstīt vispārīgu prefiksu saspiešanas metodi. 
        5. Aprakstīt empīriskus saspiešanas rezultātus (biti uz 1 simbolu dažādās valodās)
        6. Pamatot, kāpēc Hofmana algoritms ir optimāls - vidējais koda garums uz vienu simbolu vismazākais, ja salīdzina ar citām prefiksu metodēm.
        7. Definēt vidējā "prefiksa" garumu $M = \sum_{x \in X} p_x\ell_x$. 
        8. Aprakstīt, kā prefiksu koda garums atšķiras no entropijas.
    3. Aprakstīt aritmētisko saspiešanu.
        1. Piekārtot vārdiem alfabētā intervālus no $[0;1]$ 
        2. Pamatot viennozīmīgas atkodēšanas iespēju.
        3. Atrast intervālu garumus un to kodēšanai nepieciešamo bitu skaitu.
    4. Lietot Lempela-Ziva metodi.
    5. Lietot un analizēt Berouza-Vīlera algoritmu.
        1. Definēt sufiksu koku datu struktūras.
        1. Aprakstīt Berouza-Vīlera transformāciju un tai inverso.
        2. Veidot Berouza-Vīlera transformācijas.
    6. Salīdzināt "reālās dzīves" saspiešanas rīkus un bibliotēkas, to izmantotos algoritmus.
        1. Raksturot LZ77 saimes rīkus - `gz`, `WinZIP`, GIF, biroja failu formātus.   
*Pārbaude:* Kādos apstākļos nosauktie rīki pilda to pašu saspiešanu/atspiešanu, kādos apstākļos tie atšķiras.
        2. Raksturot Berouza-Vīlera algoritmu rīkus, piemēram, `bzip2`.
        3. Raksturot jaukta veida bezzudumu saspiešanu, piemēram, PNG.
        4. Paredzēt gaidāmo rezultātu, ja arhīva fails datortīklā nosūtīts ne līdz galam vai arī tajā ir daži sabojāti baiti. 
    7. **Papildtēma:** Advancēta failu saspiešana un atspiešana. 
        1. Raksturot *File binder* programmas - pašatarhivējošus izpildāmos failus.  
*Pārbaude:* Nosaukt rīkus, ar kuriem var izveidot *File binder* arhīvus. Pazīt kontekstus, kuros tos ir saprātīgi lietot.
        2. Raksturot *polymprhpic engine/polymorphic packer* - kā arhivēties katru reizi citādāk, lai vīrusi kļūtu polimorfi un varētu noslēpties no signatūru skenēšanas ((Mutation Engine, TridenT Polymorphic Engine (MtE), NuKE Encryption Device (NED), Dark Angel's Multiple Encryptor (DAME).)  
*Pārbaude:* Atšķirt Antivīrusu rīku metodes, kas ir efektīvas parastiem un polimorfiem vīrusiem.
2. Lietot un analizēt zudumradošās saspiešanas algoritmus.
    1. Aprakstīt mediju datu formātos glabājamās datu struktūras. 
        1. Aprakstīt rastra attēlu glabāšanai un apstrādei nepieciešamos datus.   
*Pārbaude:* Atrast krāsas pēc RGB koordinātēm. Definēt alfa caurspīdību kā rastra attēlu superpozīcijas/pārklāšanas koeficientu.
        2. Aprakstīt zudumradošās saspiešanas uzdevumu.  
*Pārbaude:* Definēt JPEG un līdzīgiem algoritmiem iespējamos saspiešanas parametrus.
    2. Aprakstīt pašu JPEG saspiešanas algoritmu.
3. Lietot un analizēt kļūdu korekcijas algoritmus
    1. Lietot Heminga kodus
    2. Lietot Rīda-Solomona kodus un polinomu interpolāciju.
    3. Izmantot kļūdu atjaunošanas kodējumu divdaļīgā grafā.
4. Lietot un analizēt lineārās programmēšanas algoritmus
    1. Izmantot Lineāro programmēšanas algoritmu veselos skaitļos. 
5. Lietot un analizēt virkņu meklēšanas algoritmus
    1. Veidot datu struktūras Knuta-Morisa-Prata algoritumam
    2. Veidot datu struktūras Bojera-Mūra algoritmam



