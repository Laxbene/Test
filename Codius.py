print("ZAHLENRATESPIEL")
print("----------------")

geheime_zahl = 7
versuche = 0

while True:
    tipp = input("Rate eine Zahl von 1 bis 10: ")

    if not tipp.isdigit():
        print("Bitte nur Zahlen eingeben!")
        continue

    tipp = int(tipp)
    versuche = versuche + 1

    if tipp == geheime_zahl:
        print("Richtig!")
        print("Du hast", versuche, "Versuche gebraucht.")
        break
    elif tipp < geheime_zahl:
        print("Zu klein!")
    else:
        print("Zu groß!")
