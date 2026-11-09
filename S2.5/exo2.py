tableur= int(input("Veuillez entrer le nombre dont vous voulez la table de multiplication: "))
compteur=0
while compteur<=10:
    print(f"{tableur}*{compteur} = {tableur*compteur}")
    compteur+=1
    
    #alternative 2
for compte in range(11):
    print(f"{tableur}*{compte} = {tableur*compte}")