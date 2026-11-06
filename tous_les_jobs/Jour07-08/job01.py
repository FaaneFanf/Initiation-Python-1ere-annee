# créer un programme qui affiche un rectangle
# donner une référence pour la largeur
# donner une référence pour la hauteur
# faire en sorte que la largeur s'affiche à doite et à gauche
# aller a la ligne
# afficher le résultat

# definir un programme (largeur, hauteur)
    # definir la valeur de la largeur = "-"
    # definir la valeur de la hauteur  = "|"
    # nombre = largeur
    # ligne = valeur hauteur and espace and valeur largeur * nombre and espace and valeur hauteur
    # affiche ligne 
   

#lancer le programme

# def draw_rectangle(width, height):
#     width = "-"
#     height = "|"
#     space = " "
#     nombre = width
#     ligne = height * 1, space, (width*nombre), space, height*1
#     print(ligne*height)

# draw_rectangle(10, 3)

#definir une fonction (largeur, hauteur)
    # pour chaque valeur de la hauteur
    # faire apparaitre une ligen qui affiche (| et - (multiplié par la valeur "largeur" - 2 (pour coller a l'exemple)) + |)
    # créer une boucle

def draw_rectangle(width, height):
    for i in range(height):
        print ("|" + "-" * (width-2) + "|")

draw_rectangle(24, 12)
