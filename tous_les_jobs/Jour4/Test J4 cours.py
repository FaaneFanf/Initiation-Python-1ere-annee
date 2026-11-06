# Fonction
# def my_name():
#     print("Je suis alex")
# my_name()

# # Return
# def getHello():
#     return "Hello tout le monde"
# message = getHello()
# print(message)

# # Fonctions sans paramètres
# def afficher_message():
#     print("Bonjour comment ca va ?")

# afficher_message()

# # Fonction avec paramètres
# def afficher_nom_prenom(nom, prenom):
#     print("nom :", nom)
#     print("prenom :", prenom)
# afficher_nom_prenom("Dupont", "Jean")

# # Fonction avec valeur de retour
# def calculer_somme(a, b):
#     resultat = a + b
#     return resultat 
# somme = calculer_somme(10, 7)
# print(somme)

# x = "hello"
# def test():
#     print(x)

# test()
# print(x)

# x = False
# def test():
#     x = "Hello"

# test()
# print(x)

# fonction addition et à l'intérieru récuperer un input dans une variable (un chiffre). Et ensuite print ce chiffre x10
#Dans la fonction addition je récupère un input et je print le chiffre que j'ai prus en input x10

# def add():
#     resultat = int (input("Quel nombre ?"))
#     print(resultat*10)
# add()

# x = int(input("Quel es votre nombre ? : "))

# def add(x):
#     resultat = x * 10
#     print(resultat)

# add(x)

# x = int(input("Quel es votre nombre ? : "))
# y = int(input("Quel es votre nombre ? : "))

# def add(x, y):
#     resultat = x + y
#     print(resultat)

# add(x, y)

x = int(input("Quel es votre nombre ? : "))

def add(x):
    resultat = x * 10
    return resultat

somme = add(x)
print(somme)
