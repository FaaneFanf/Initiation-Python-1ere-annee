L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

def calc():
    produit = 1
    for nombre in L:
        if nombre <= 25 and nombre <= 90:
            produit = produit * nombre
            print(produit)
    

calc()
