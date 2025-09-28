# python-slutuppgift
Slutuppgift för kurs - Systemutveckling med python 

Slutuppgiften går ut på att skriva en övervakningsapplikation skriven i Python. Applikation samlar in information från operativsystemet och presenterar informationen för en användare.

En användare kan interagera med applikationen via en konsol för att få fram information om CPU användning, minnesanvändning, diskanvändning. När användaren interagerar med applikationen via konsolmenyn ska inga konfigurerade larm aktiveras.

-------Kraven på applikationen för godkänd nivå-------
Applikationen startas, och sedan presenteras användaren med fem stycken alternativ i konsolen:

1. Starta övervakning
Startar övervakning av CPU användning, minnesanvändning och diskanvändning. Notera alltså att ingen övervakning ska starta automatiskt vid programstart.

2. Lista aktiv övervakning
Listar aktiv övervakning som är aktiv samt nuvarande övervakningsstatus. Har man inte startat övervakningen ska en text visas som informerar användaren om att ingen övervakning är aktiv. Annars visas övervakningen, t.ex:

-CPU Anvädning: 35%
-Minnesanvändning: 65% (4.2 GB out of 8 GB used)
-Diskanvändning: 80% (400 GB out of 500 GB used)

Efter detta promtas användaren om att bekräfta genom att trycka enter, "Tryck valfri tangent för att gå tillbaka till huvudmeny".
Efter detta visas åter huvudmenyn för användaren.

3. Skapa larm
Väljer man detta alternativ får man upp ytterligare en meny där man får välja att konfigurera larm inom tre områden eller gå tillbaka till huvudmenyn.

-Konfigurera larm

1.CPU användning
2.Minnesanvändning
3.Diskanvändning
4.Tillbaka till huvudmeny

Efter att man valt ett alternativ får man välja en procentuell nivå där larmet ska aktiveras. T.ex. "Ställ in nivå för alarm mellan 0-100".
Efter att användaren har valt en nivå skrivs en bekräftelse ut, sedan visas huvudmenyn igen.
Larm för CPU användning satt till 80%. 
Nivån måste matas in som en siffra mellan 1-100 och matas nonsens in ska användaren få ett felmeddelande.

4. Visa larm
Listar alla configurerade larm. Larmen ska vara sorterade på typ när de visas. Exempel:

1.CPU larm 70%
2.Disklarm 95%
3.Minneslarm 80%
4.Minneslarm 90%

Efter detta promtas användaren om att bekräfta genom att trycka enter, "Tryck valfri tangent för att gå tillbaka till huvudmeny".
Notera att man kan ha flera larm av samma typ.

5. Starta övervakningsläge
Startar ett övervakningsläge. Användaren blir promtad om att övervakningsläget har startats, sedan loopar en sträng med jämna mellanrum som meddelar användaren att övervakningen är aktiv samt att man på något sätt kan återgå till huvudmenyn.

Övervakning är aktiv, tryck på valfri tangent för att återgå till menyn.

                Triggas ett larm när övervakningen är aktiv skrivs det ut i konsolen. T.ex:
                ***VARNING, LARM AKTIVERAT, CPU ANVÄNDNING ÖVERSTIGER 80%***

-------Icke funktionella krav på applikationen för G nivå-------
1.Programmet ska bestå av minst ett antal filer med kod som aktivt används. Dvs. All kod ska inte vara skriven i en fil.
2.Programmet ska använda sig av objekt där det passar.
3.Programmet ska vara skrivet med funktioner.
4.Programmet ska innehålla funktionell programmering på minst ett ställe. T.ex. vid sortering av larm innan visning.
5.Koden ska vara välskriven, dvs. Lättförståliga variabelnamn och funktionsnamn, kommentarer där det passar och en bra struktur.
6.Koden ska självklart vara bugfri. Dvs. funktionaliteten som beskrivs ska alltid fungera korrekt.
7.Koden ska kunna hantera att användaren matar in felaktig input / nonsens utan att gå sönder. Dvs. rimlig input sanitization ska finnas.

 
-------Kraven på applikationen för väl godkänd nivå-------
För väl godkänd nivå krävs att man lägger till tre funktioner i programmet. För det första ska loggning läggas tiill. Dvs alla händelser i programmet från programstart, all användarinout, alla configurationsförändringar ska sparas i en logfil.

Allt som loggas till logfilen ska innehålla:
-Datum _Tid _ Log. T.ex.
-20/9/2024_15:05_CPU_Användningslarm_Konfigurerat_80_Procent
-20/9/2024_15:09_Övervakningsläge_startat
-20/9/2024_15:16_CPU_Användningslarm_aktiverat_80_Procent

6. Ta bort alarm
Den andra funktionaliteten som ska läggas till är förmågan att ta bort konfigurerade alarm. Detta görs genom ett nytt menyval för att ta bort alarm.
Väljer man detta alternativ får man upp en lista med larm som är konfigurerade. Sedan kan man välja ett larm att ta bort genom att trycka på motsvarande siffra. T.ex.

Välj ett konfigurerat larm att ta bort:
5.CPU larm 70%
6.Minneslarm 80%
7.Minneslarm 90%
8.Disklarm 95%

Efter att man har tagit bort ett larm går man tillbaka till huvudmenyn.

Det sista som läggs till är att alla larm som skapas och persisteras till disk. Dvs. Sparas i ett lämpligt filformat (json). När programmet startas laddas tidigare konfigurerade larm och texten loading previously configured alarms...

Notera att detta påverkar G delens menyalternativ, väljer man t.ex. att visa alla aktiva alarm ska både de som konfigurerats under körning och de som har lästs in vid uppstart av programmet visas.

-------Icke funktionella krav för VG nivå-------
Alla krav för godkänd nivån samt:

Koden ska vara mycket välskriven, dvs. Lättförståliga variabelnamn och funktionsnamn, kommentarer där det passar och en mycket bra struktur. Detta gäller även logfiler.

Exempel på detta är att om man har flera CPU användningslarm konfigurerade ska enbart det närmaste aktiveras. Dvs. Har man satt upp larm som aktiveras vid CPU användning på 60%, 70% och 80% ska endast 80% nivån aktiveras om CPU användningen skulle hoppa upp på 95% vid en mätpunkt.

Ett annat exempel är att logfiler skapas och sparas varje gång programmet startas. Dessa namnges dynamiskt baserat på datum och tid när logfilen skapades och sedan fylls de på så länge programmet körs.

-------Valfria tillägg till uppgiften. (Plus i kanten)-------
1. Skicka ett mejl vid aktiverade larm. (Tips använd sendgrid, man kan registrera sig gratis på sendgrid.com och få tillgång till ett antal mejl varje månad) Detta gör programmet mer användbart! Kul! Bibliotek som behövs:

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

2. Versionshantera hela utvecklingen på GitHub. Använd trunkbaserad utveckling och skapa feature branches för varje ny funktionalitet som läggs till i programmet. Starkt rekommenderat för alla oavsett G eller VG nivå.
 

3. Skapa ett enkelt grafiskt gränssnitt till applikationen som visar aktiva larm samt procentuella nivåer i realtid.
