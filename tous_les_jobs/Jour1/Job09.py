produit1 = "Café"
prix_unitaire = 6
quantité_stock = 12
total = prix_unitaire * quantité_stock

print("produit1 :" "café")
print("prix_unitaire :", 6, "€")
print("quantité_stock :", 12)
print("Total :", total, "€")

produit2 = "bonbons"
prix_unitaire2 = 3
quantité_stock2 = 8
total2 = prix_unitaire2 * quantité_stock2

print("produit2 :" "bonbons")
print("prix_unitaire2 :", 3, "€")
print("quantité_stock2 :", 8)
print("Total2 :", total2, "€")  

produit3 = "céréales"
prix_unitaire3 = 4
quantité_stock3 = 50
total3 = prix_unitaire3 * quantité_stock3

print("produit3 :" "céréales")
print("prix_unitaire3 :", 4, "€")
print("quantité_stock3 :", 50)
print("Total3 :", total3, "€")

achat = input("Quelle quantité de céréales voulez-vous acheter ? ")
achat = int(achat)

stock = quantité_stock3 - achat
print("Il reste", stock, "céréales en stock.")

produit3 = "céréales"
prix_unitaire3 = 4
print("ancien prix :", 4, "€")
prix = prix_unitaire3 * 1.10
print("nouveau prix :", prix, "€")
