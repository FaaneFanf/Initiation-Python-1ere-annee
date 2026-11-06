montant_initial = 10000
taux_de_rendement = 5
print("Capital initial :", montant_initial, "€")
print("Taux initial :", taux_de_rendement, "%")
print("Gain annuel :", montant_initial * taux_de_rendement / 100, "€")

capital = montant_initial + 5000
taux = taux_de_rendement + 2
print("Capital après augmentation :", capital, "€")
print("Taux après augmentation :", taux, "%")
print("Gain après augmentation du capital et du taux :", capital * taux / 100, "€")

capital = capital - (capital * 0.1)
taux = taux - 1
print("Capital après diminution :", capital, "€")
print("Taux après diminution :", taux, "%")
print("Gain après diminution du capital et du taux :", capital * taux / 100, "€")
print("Gain final :", capital * taux / 100, "€")

