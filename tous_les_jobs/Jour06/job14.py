
def my_long_word(nombre, phrase):
    resultat = ""
    mot = ""

    for caractere in phrase: #On lit chaque caractère un par un.
        if caractere != " ": #Tant que ce n'est pas un espace, on ajoute le caractère au mot
            mot += caractere
        else:
            # Comptage manuel des lettres
            compteur = 0
            for lettre in mot:
                compteur += 1 #Chaque lettre ajoute 1 au compteur.

            if compteur > nombre: #Si la taille du mot est supérieure au nombre demandé
                resultat += mot + " " #on l'ajoute au résultat

            mot = ""

    # Vérifier le dernier mot
    compteur = 0
    for lettre in mot:
        compteur += 1

    if compteur > nombre:
        resultat += mot

    return resultat


texte = "La peur est le chemin vers le cote obscur la peur mene a la colere la colere mene a la haine la haine mene a la souffrance"

print(my_long_word(1, texte))