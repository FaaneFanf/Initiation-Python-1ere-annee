n = int(input("Entrez un nombre : "))
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")


n = int(input("Entrez un nombre : "))
print(f"Table de multiplication de 1 à {n} :")

for i in range(1, n + 1):
    print(f"Table de multiplication de {i} :")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Ligne vide pour séparer les tables de multiplication


i = 1
n = 1
table = int(input("Entrez un nombre pour afficher sa table de multiplication : "))
while i <= table:
    for i in range(1,11):
        print(f"{table} x {i} = {table * i}")
    i += 1  
