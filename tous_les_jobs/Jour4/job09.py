# x = int(input())
# y = int(input())
# z = int(input())

# def average(x, y, z):
#     return x + y +z
# def moyenne_etudiant():
#     for x in range(0, 21):
#         x = int(input("Note1 :"()))
#     for y in range(0, 21):
#         y = int(input("Note2 :"()))  
#     for z in range(0, 21):
#                 z = int(input("Note3 :"()))      
#     moyenne = (x+y+z)/3
#     print(moyenne)

            
        # moyenne = (x+y+z)/3    
        # print(moyenne)
        # if 15 <= moyenne <= 20:
        #     print("Très bon élève")
        # elif 14 <= moyenne <= 11:
        #     print("Bon élève")
        # elif 10 <= moyenne <= 8:
        #     print("Elève moyen")
        # elif 7 <= moyenne <= 0:
        #     print("Elève devant faire des efforts")


def average(note1, note2, note3):
      return (note1 + note2 + note3)/3

note1 = int(input("Note 1 : "))
note2 = int(input("Note 2 : "))
note3 = int(input("Note 3 : "))

moyenne_etudiant = average(note1, note2, note3)

print("Moyenne :", moyenne_etudiant)

if 15 <= moyenne_etudiant <=20:
    print("Très bon élève")
elif 11 <= moyenne_etudiant <= 14:
    print("Bon élève")
elif 8 <= moyenne_etudiant <= 10:
     print("Elève moyen")
elif 0 <= moyenne_etudiant <= 7:
     print("Elève devant faire des efforts")
