def message_code(message: str, dec: int):
    abc = "abcdefghijklmnopqrstuvwxyz"
    new_string = ""
    for i in range(len(message)):
        if abc.find(message[i]) > -1:
            ind = (abc.index(message[i]) + dec) % 26
            new_string += (abc[ind])
        else : new_string += message[i]

    return new_string

mon_message = "salut jeune entrepreneur"
mon_message = message_code(mon_message, 3)
print(mon_message)
print(message_code(mon_message, -3))
