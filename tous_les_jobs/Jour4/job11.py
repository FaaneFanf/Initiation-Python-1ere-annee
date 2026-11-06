# def time_to_text(minutes):
#     heures = minutes // 60
#     reste_minutes = minutes % 60
#     print (heures, "heures et", reste_minutes, "minutes")

# time_to_text(168)

# // : division entière et % : reste de la division


def time_to_text(x):
    x = int(input("Combien de minutes ? : "))
    heures = x //60
    reste = x % 60
    print (heures, "heures et", reste, "minutes")

time_to_text(268)   
