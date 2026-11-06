# num1 = int(input("Quel est le nombre ? :"))
# num2 = int(input("Quel est le nombre ? :"))
# operator = input("choisir l'opération"))

# def any_computation(num1,num2, operator);
#     if operator =="+":
#         resultat = num1 + num2
#     if operator == "-":
#         resultat = num1 - num2
#     if operator == "*":
#         resultat =  num1 * num2
#     if operator == "/":
#         resultat = num1 / num2



#     return resultat

# resultat = any_computation(num1, num2, operator)

# print(resultat)

def any_computation(num1, num2, operator):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 + num2
        case "*":
            return num1 * num2
        case "/":
            return num1 + num2
        case "%":
            return num1 + num2
        case _:
            return ("mauvais caractère")

num1 = float(input("num1 = "))
num2 = float(input("num2 = "))
operator = input("choisir l'opérateur : ")

resultat = any_computation(num1, num2, operator)
print(resultat)






# def any_computation():
#     num1 = 6
#     operator = "+"
#     num2 = 8
#     resultat = num1 + num2
#     print(resultat)

# any_computation()