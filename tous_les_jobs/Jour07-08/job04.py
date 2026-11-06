# Créer une fonction à laquelle on donne un message et un décalage, et la
# fonction renvoie alors le message décalé dans l'alphabet. Il faudra gérer le
# dépassement (« z » décalé vers la droite revient sur « a », et « a » décalé vers
# la gauche revient sur « z »).


# créer un fonction message_code
#  inclure un input = (taper votre message)
#  créer une variable avec les lettres alphabet = "abcdefghijklmnopqrstuvwxyz"
#  pour chaque lettre présente dans le message, décaler de 3 rangs la lettre
#  comment inclure les espaces ?
#  
# etape 1 = taper le message
# etape 2 = coder le message
# etape 3 = afficher le message coder
#  
# exemple = "Bon" devient "B=E O=R N=Q" message codé = ERQ = BON
# 
# a = d
# b = e
# c = f
# d = g
# e = h
# f = i
# g = j
# h = K
# i = l
# j = m
# def message_code():
#     message = input("Quel est votre message ? : ")
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
# if alphabet [1, 26]:
#         new_alphabet = alphabet[+3]
#         for i in range(len(alphabet)):
#             code = message 
#             print(code)

# message_code()


# def message_code():
#     message = input("Quel est votre message ? : ")
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for lettre in message : 
#         print(lettre)

#     position = alphabet.index(lettre)
#     nouvelle_position = position + 3
#     nouvelle_lettre = alphabet[nouvelle_position]
#     message_code = ""
#     for lettre in message:
#         position = alphabet.index(lettre)
#         nouvelle_position = position + 3
#         message_code = message_code + alphabet[nouvelle_position]
#         print(message_code)
    
# message_code()

# def cesar(message, decalage):
#     result = ""

#     i = 0
#     while i < len(message):
#         value = ord(message[i]) + decalage
#         # message[i] = chr(value)
#         result += chr(value)
#         i += 1

#     return result

# result = cesar("bonjou", 12)
# print(result)

def cesar(message, n):
    result = ""


    i = 0
    while i < len(message):
        value = ord(message[i])


        if (value >= 97 and value <= 122):
            while value + n > 122:
                n -= 122 - value
                value = 97


            value += n


            result += chr(value)
        else:
            result += message[i]


        i += 1


    return result


result = cesar("tristan ne me donne pas de phrase", 1)
print(result)




def cesar(message, n):
    result = ""
    i = 0
    while i < len(message):
        value = ord(message[i])

        print (message[i])

        if (value > 97 and value <= 122):
            while value + n > 122:
                n -= 122 - value
                value = 97
    
        value += n

        result.add(chr(value))
    else:
        result += message[i]
    
        i += 1

    return result

result = cesar("bonjour", 4)
print(result)
