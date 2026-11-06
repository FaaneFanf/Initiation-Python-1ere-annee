socreA = int(input("quel est le scoreA ?"))
scoreB = int(input("quel est le scoreB ?"))

for scoreA in range(1, 100):
    def gagnant(scoreA, scoreB): 
     if scoreA > scoreB:
        vainqueur = "equipeA"
     elif scoreA < scoreB:
        vainqueur = "equipeB"
     else:
        vainqueur = "match nul"
     return vainqueur