liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Arrondi manuel
arrondis = []

for nombre in liste:
    entier = int(nombre) #Récupère la partie entière
    decimal = nombre - entier #Calcule la partie décimale.

    if decimal >= 0.5: #Si la décimale vaut au moins 0,5, on arrondit au supérieur
        arrondis.append(entier + 1) #append() est une méthode de liste qui sert à ajouter un élément à la fin d'une liste
    else:
        arrondis.append(entier)

# Tri à bulles sans sort() ni len()
taille = 0

for _ in arrondis:
    taille += 1

for i in range(taille):
    for j in range(taille - 1 - i):
        if arrondis[j] > arrondis[j + 1]:
            temp = arrondis[j]
            arrondis[j] = arrondis[j + 1]
            arrondis[j + 1] = temp

print(arrondis)