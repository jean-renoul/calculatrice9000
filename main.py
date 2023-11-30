nombres = []
historique = []

def data():

    a = input("Entrez un nombre : ")
    nombres.append(a)
    historique.append(a)
    while True:
        a = input("Entrez un nombre ou un opérateur : ")
        nombres.append(a)
        historique.append(a)
        if a == "=":
            return nombres

def calculette():

    data()
    i = 1
    while i < len(nombres):
        if nombres[i] == "*":
            nombres[i - 1] = (float(nombres[i - 1]) * float(nombres[i + 1]))
            del nombres[i:i+2]
        elif nombres[i] == "/":
            if nombres[i + 1] == "0":
                print ("Vous ne pouvez pas diviser par 0")
                nombres.clear()
                calculette()

            else:
                nombres[i - 1] = (float(nombres[i - 1]) / float(nombres[i + 1]))
                del nombres[i:i+2]
        else:
            i += 1

    i = 1
    while i < len(nombres):
        if nombres[i] == "+":
            nombres[i - 1] = (float(nombres[i - 1]) + float(nombres[i + 1]))
            del nombres[i:i+2]
        elif nombres[i] == "-":
            nombres[i - 1] = (float(nombres[i - 1]) - float(nombres[i + 1]))
            del nombres[i:i+2]
        else:
            i += 1
    print (float(nombres[0]))
    historique.append(float(nombres[0]))
    nombres.clear()


    afficher_historique = input("Voulez-vous afficher l'historique ? (oui/non)")
    if afficher_historique == "oui":
        print (historique)
    else:
        calculette()

    input_effacer_historique = input ("Voulez-vous supprimer cet historique ? (oui/non)")
    if input_effacer_historique == "oui":
        effacer_historique()
    else:
        calculette()


def effacer_historique():
    historique.clear()

calculette()

