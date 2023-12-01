# Liste pour stocker les nombres et l'historique des opérations
nombres = []
historique = []

# Fonction pour saisir les nombres et les opérateurs
def data():
    # Saisir le premier nombre
    a = input("Entrez un nombre : ")
    nombres.append(a)
    historique.append(a)

    # Saisir les nombres ou opérateurs jusqu'à ce que "=" soit entré
    while True:
        a = input("Entrez un nombre ou un opérateur : ")
        nombres.append(a)
        historique.append(a)
        if a == "=":
            return nombres

# Fonction principale pour effectuer les calculs
def calculette():
    # Appeler la fonction pour saisir les données
    data()

    # Première boucle pour traiter les multiplications et divisions
    i = 1
    while i < len(nombres):
        if nombres[i] == "*":
            nombres[i - 1] = (float(nombres[i - 1]) * float(nombres[i + 1]))
            del nombres[i:i+2]
        elif nombres[i] == "/":
            # Interdire la division par zéro
            if nombres[i + 1] == "0":
                print("Vous ne pouvez pas diviser par 0")
                nombres.clear()
                calculette()
            else:
                nombres[i - 1] = (float(nombres[i - 1]) / float(nombres[i + 1]))
                del nombres[i:i+2]
        else:
            i += 1

    # Deuxième boucle pour traiter les additions et soustractions
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

    # Afficher le résultat, ajouter le résultat à l'historique et nettoyer la liste nombres
    print(float(nombres[0]))
    historique.append(float(nombres[0]))
    nombres.clear()

    # Demander à l'utilisateur s'il veut afficher l'historique
    afficher_historique = input("Voulez-vous afficher l'historique ? (oui/non)")
    if afficher_historique == "oui":
        print(historique)
    else:
        calculette()

    # Demander à l'utilisateur s'il veut effacer l'historique
    input_effacer_historique = input("Voulez-vous supprimer cet historique ? (oui/non)")
    if input_effacer_historique == "oui":
        effacer_historique()
        calculette()
    else:
        calculette()

# Fonction pour effacer l'historique
def effacer_historique():
    historique.clear()

# Appeler la fonction principale pour démarrer la calculatrice
calculette()