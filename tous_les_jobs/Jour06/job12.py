

# def tri(liste, taille):
#     for i in range(taille - 1):
#         for j in range(taille - 1 - i):
#             if liste[j] > liste[j + 1]:
#                 temp = liste[j]
#                 liste[j] = liste[j + 1]
#                 liste[j + 1] = temp

#     return liste


# nombres = [8, 3, 1, 6, 2]
# resultat = tri(nombres, 5)

# print(resultat)

def tri(liste, taille):
    for i in range(100):
        for j in range(taille - 1):
            if liste[j] > liste[j + 1]:
                sauvegarde = liste[j]
                liste[j] = liste[j + 1]
                liste[j + 1] = sauvegarde
    return liste

nombres = [16, 95, 1, 13, 5, 62, 9, 14, 2, 23]
resultat = tri(nombres, 10)

print(resultat)

