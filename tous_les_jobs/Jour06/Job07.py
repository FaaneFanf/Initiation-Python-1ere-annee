L = [8, 24, 48, 2, 16]

def mult3():
    L = [8, 24, 48, 2, 16]
    compte = 0
    for nombre in L:
        if nombre %3 == 0:
           compte += 1
    
    print (compte)

mult3()
