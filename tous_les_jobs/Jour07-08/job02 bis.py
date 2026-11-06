#Écrire un programme qui affiche dans la console un triangle avec des « _ »,
#des « \ » et des « / » en fonction de l’input entré, qui représentera la hauteur.

# afficher un triangle avec :
    # / pour le côté gauche
    # \ pour le côté droit
    # _ pour la base

# ligne 1 :    /\       = 4 espace avant triangle  /0 espace dans le triange
# ligne 2 :   /  \      = 3 espaces avant triangle / 2 espace
# ligne 3 :  /    \     = 2 espaces avant triangle / 4 espace
# ligne 4 : /      \    = 1 espaces avant triangle / 6 espace
# ligne 5 :/________\   = 0 espace aavant triangel / _ * 8


# les espaces devant le triangle diminue à chaque ligne
# les espaces dans le triangle augmentent à chaque ligne

#la première ligne print = " " * 4 + "/" + " " * 0 + "\\"
#la deuxième ligne print = " " * 3 + "/" + " " * 2 + "\\"

# il faut créer une boucle pour les ligne en fonction de la hauteur
# for ligne in range(1, X) compte de 1 à la valeur de la hauteur x

# il faut créer les côtés.
# il faut créer la base
# 
# pour les côtés : il faut créer les espaces.
#  espace_devant = la taille de la hauteur - le numéro de la ligne (diminue de 1 à chaque boucle)
# pour les espaces au milieu : il faut créer des espaces
#  espace_milieu = numero de ligne - 1 * 2 
# 
# il faut print la boucle = print (" " * espace_devant + "/" + " " * espace_milieu ++ "\\")
#
# il faut faire la base du triangle
# le nombre de _ depend de la taille du triange
# dans l'exemple de hauteur de 5 c'est 8 trait. 
# donc c'est la (hauteur - 1) * 2
# il faut finir la boucle par cet affichage
# il faut print la formule = ("/ + "_" * (hauteur -1)*2 + "\\")

# il faut créer un programme qui demande la hauteur et qui inclus toutes nos conditions.


def triangle():
    hauteur = int(input("Quelle est la hauteur du triangle ? : "))   
    for ligne in range(1, hauteur):
        espace_devant = hauteur - ligne
        espace_milieu = (ligne - 1) * 2
        print (" " * espace_devant + "/" + " " * espace_milieu + "\\")
    print ("/" + "_" * (hauteur - 1)*2 + "\\")    

triangle()

