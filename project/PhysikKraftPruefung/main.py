from schueler import Schueler
from fragen import Fragen
from random import choice, shuffle

name = input("Gib deinen Namen ein und schließe mit Enter ab. Name: ")

tester = Schueler(name)

frage = []

#Sammlung der Fragen
####################
#Frage 1
frage.append(Fragen("Umrechnung von m in cm"))
moegliche_werte_meter = [3,8,2.5,12.13,2.06]
zufallswert = choice(moegliche_werte_meter)
frage[0].set_fragestellung("Wieviel cm sind " + str(zufallswert) + "m")
frage[0].set_antwort(str(int(zufallswert * 100)))

#Frage 2
frage.append(Fragen("Umrechnung von cm in m"))
moegliche_werte_zentimeter = [9200,345,679,7408]
zufallswert = choice(moegliche_werte_zentimeter)
frage[1].set_fragestellung("Wieviel m sind " + str(zufallswert) + "cm. Bitte benutze einen Punkt für das Komma, z.B. 150cm = 1.50m.")
frage[1].set_antwort(str(zufallswert / 100))

#Frage 3
frage.append(Fragen("Umrechnung von g in kg"))
moegliche_werte_gramm = [851,7000,2831,879266,395,19200]
zufallswert = choice(moegliche_werte_gramm)
frage[2].set_fragestellung("Wieviel kg sind " + str(zufallswert) + "g. Bitte benutze einen Punkt für das Komma, z.B. 150cm = 1.50m.")
frage[2].set_antwort(str(zufallswert / 1000))

#Frage 4
frage.append(Fragen("Was ist physikalische Kraft"))
frage[3].set_fragestellung("Welche der Begriffe Willenskraft, Gewichtskraft, Waschkraft bezeichnet eine physikalische Kraft?")
frage[3].set_antwort("Gewichtskraft")
frage[3].set_punkte(2)

#Frage 5
frage.append(Fragen("Was ist physikalische Kraft"))
frage[4].set_fragestellung("Welche der Begriffe Waschkraft, Schaffenskraft, Federkraft bezeichnet eine physikalische Kraft?")
frage[4].set_antwort("Federkraft")
frage[4].set_punkte(2)

#Frage 6
frage.append(Fragen("Was ist physikalische Kraft"))
frage[5].set_fragestellung("Welche der Begriffe Muskelkraft, Überzeugungskraft, Reibungskraft bezeichnet keine physikalische Kraft?")
frage[5].set_antwort("Überzeugungskraft")
frage[5].set_punkte(2)

#Frage 7
frage.append(Fragen("Kraft bewirkt Beschleunigung"))
frage[6].set_fragestellung("Im folgenden Text fehlt ein Wort. Dies ist durch #### dargestellt. Schreibe das richtige Wort. Achte auf Rechtschreibung.\n\nWenn wir bei einem Wettlauf starten oder einen Fußball anhalten, wirkt eine Kraft. Eine Kraft bewirkt eine ####.")
frage[6].set_antwort("Beschleunigung")
frage[6].set_punkte(3)

#Frage 8
frage.append(Fragen("Kraft bewirkt Richtungsänderung"))
frage[7].set_fragestellung("Im folgenden Text fehlt ein Wort. Dies ist durch #### dargestellt. Schreibe das richtige Wort. Achte auf Rechtschreibung.\n\nWenn wir uns in einem Karussell mit gleicher Geschwindigkeit drehen, wirkt eine Kraft. Eine Kraft bewirkt eine #### der Bewegungsrichtung.")
frage[7].set_antwort("Änderung")
frage[7].set_punkte(3)

#Frage 9
frage.append(Fragen("Kraft bewirkt Verformung"))
frage[8].set_fragestellung("Im folgenden Text fehlt ein Wort. Dies ist durch #### dargestellt. Schreibe das richtige Wort. Achte auf Rechtschreibung.\n\nWenn wir gegen einen Sandsack boxen oder ein Lineal biegen, wirkt eine Kraft. Man kann das Wirken einer Kraft an der #### eines Körpers erkennen.")
frage[8].set_antwort("Verformung")
frage[8].set_punkte(3)

#Frage 10
frage.append(Fragen("Welche Kraftwirkung"))
frage[9].set_fragestellung("Welche der Kraftwirkungen Beschleunigung, Richtungsänderung, Verformung sehen wir im folgenden Beispiel?\n Eine Person springt von einem Turm ins Wasser.")
frage[9].set_antwort("Beschleunigung")
frage[9].set_punkte(2)


print("\nHallo " + tester.name + ". Willkommen zu ein paar Fragen zur Physik.\n\n")
print("Es gibt Fragen zur Umrechnung von Einheiten. In der eingegebenen Lösung lässt du die Einheit weg.\nBei den Fragen, wo du ein Wort eingeben musst, muss das Wort auf jeden Fall richtig geschrieben werden.\n VIEL ERFOLG\n ###########")

shuffle(frage)
gesamtpunkte = 0
for i in range(len(frage)):
    antwort = frage[i].stelle_frage()
    gesamtpunkte = gesamtpunkte + frage[i].punkte
    if antwort:
        tester.set_punkte(tester.punkte + frage[i].punkte)
        print("\nDas ist korrekt " + tester.name + ". Weiter so.")
    else:
        print("Die Antwort ist leider falsch. Achte bei der Eingabe auf richtige Zahlen oder richtige Rechtschreibung.\n")

    print("Du hast bis jetzt " + str(tester.punkte) + " von " + str(gesamtpunkte) + " Punkten erreicht.\n")

eingabe = input("Drücke Enter, um zur Auswertung zu gelangen.")
print("\n" * 100)

print("Auswertung der Fragen für " + tester.name)
print("#####################################\n\n")
print("Du hast insgesamt " + str(tester.punkte) + " von " + str(gesamtpunkte) + " Punkten erreicht.\n")

# Falls auf Trinket mal gemeinsames Arbeiten läuft, wäre das eine Idee
# auswertung_out = open(name +".txt" , "w")
# auswertung_out.write(name)
# auswertung_out.write("\nPunkte")
# print(name)
