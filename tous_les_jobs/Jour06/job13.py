
liste = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

doublons = []

for nombre in liste:
    deja_la = False

    for element in doublons:
     if nombre == element:
        deja_la = True

    if deja_la == False:
        doublons.append(nombre)

print(doublons)
