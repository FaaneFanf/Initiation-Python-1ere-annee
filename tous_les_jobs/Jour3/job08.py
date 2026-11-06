a = float(input("Quelle est la longueur du côté A : "))
b = float(input("Quelle est la longueur du côté B : "))
c = float(input("Quelle est la longueur du côté C : "))

if a == b == c:
    print("C'est un triangle équilatéral")
if a == b and a != c or b == a and b!= c or b ==c and a != c:
    print("C'est un triangle isocèle")
if a**2 == b **2 + c **2 or b **2 == a **2 + c **2 or c **2 == b **2 + a **2:
    print("C'est un triangle rectangle")
if a != b and b != c and a != c:
    print("C'est un triangle quelconque")

