# Listes pour stocker les nombres et l'historique des opérations
nombres = []
historique = []

# Fonction pour saisir les nombres et les opérateurs
def data():
    # Saisit le premier nombre, en vérifiant qu'il est bien valide
    while True:
        try:
            a = float(input("Entrez un nombre : "))
            break
        except ValueError:
            print ("Veuillez entrer un nombre valide.")

    nombres.append(a)
    historique.append(a)

    # Saisit les nombres ou opérateurs, toujours avec vérification jusqu'à ce que "=" soit entré
    while True:
        a = input("Entrez un nombre ou un opérateur (Entrez '=' pour obtenir le résultat) : ")

        if a == "=":
            nombres.append(a)
            historique.append(a)
            return nombres

        try:
            a = float(a)
            nombres.append(a)
            historique.append(a)
        except ValueError:
            if a in ['+', '-', '*', '/']:
                nombres.append(a)
                historique.append(a)
            else:
                print("Entrez un nombre valide ou utilisez '+', '-', '*', '/' pour les opérations.")



# Fonction principale pour effectuer les calculs
def calculette():
    # Appele la fonction pour saisir les données
    data()

    # Première boucle pour traiter les multiplications et divisions en premier
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

    # Affiche le résultat, ajoute le résultat à l'historique et nettoie la liste nombres pour les prochains calculs
    print(float(nombres[0]))
    historique.append(float(nombres[0]))
    nombres.clear()

    # Demande à l'utilisateur si il veut afficher l'historique
    afficher_historique = input("Voulez-vous afficher l'historique ? (oui/non)")
    if afficher_historique == "oui":
        print(historique)
    else:
        calculette()

    # Demande à l'utilisateur si il veut effacer l'historique
    input_effacer_historique = input("Voulez-vous supprimer cet historique ? (oui/non)")
    if input_effacer_historique == "oui":
        effacer_historique()
        calculette()
    else:
        calculette()

# Fonction pour effacer l'historique
def effacer_historique():
    historique.clear()

# Appele la fonction principale pour démarrer la calculatrice
calculette()