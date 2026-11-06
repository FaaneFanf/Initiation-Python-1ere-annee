# Écrire une fonction qui, recevant une taille n en paramètre, affiche un tapis de
# n+1 ligne/n+1 colonne traversé par une diagonale.
#
# definir une fonction
# => def diagonale(n):
# 
# dans l'exemple pour n = 10 il y a 10 # et un espace
# l'espace se décale vers la gauche à chaque boucle
# il y a un | en début et fin de chaque ligne
# Sur la premiere et dernière ligne on affiche : "+" + nombre total de # + " " + "+"
# chaque ligne # se compose de : "|" + combre total de n + " " + "|"
# pour n = 10 on a 13 lignes
# 1 ligne intro + 11 ligne # + 1 ligne conclusion
# ligne 1 = début de programme +------+
# ligne 2 = ligne # " "
# ligne 3 = ligne # " " #
# etc.... l'espace " " se decale d'1 à gauche à chaque ligne
# ligne 12 : " " #
# ligne 13 : +------+
# 

# def diagonale():
#     diese = int(input("Quelle est la taille ? : "))
#     intro_conslusion = ("+" + ("-" * (diese +1)) + "+")
#     for i in range(1, diese):
#         ligne_diese = ("|" + ("#") * [+1] + (" ") * [-1] + "|" )
#         print(ligne_diese)

#     print(intro_conslusion)   


# diagonale()


#texte = texte[1:] + texte[0]

# def diagonale():
#     diese = int(input("Quelle est la taille ? : "))
#     intro_conslusion = ("+" + ("-" * (diese +1)) + "+")
#     print(intro_conslusion)
#     for ligne in range(1, diese +1):
#         ligne_diese = ("|" + ("#" * diese[1:]) + diese[0] + "|") 
#         print(ligne_diese)

#     print(intro_conslusion)   


# diagonale()

def diagonale ():
    diese = int(input("Quelle est la taille ? : "))
    debut_fin = ("+" + "-" * (diese) + "+")
    print (debut_fin)
    for ligne in range(1, diese +1):
        partie_gauche = "#" * (diese -ligne)
        partie_droite = "#" * (ligne - 1)
        ligne_diese = "|" + partie_gauche + " " +partie_droite + "|"
        print (ligne_diese)
    print (debut_fin)

diagonale()
