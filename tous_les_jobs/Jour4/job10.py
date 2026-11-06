def is_odd():
    nombre = int(input("Entrer un chiffre : "))
    if nombre < 0: 
        print("Erreur")
    elif nombre %2 == 0: 
        print("Pair")
    else:
        print("Impair")

is_odd()
