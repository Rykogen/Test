def valeur():
    a=int(input("entrez la 1ère valeur: "))
    b=int(input("entrez la 2e valeur: "))
    return a,b 
    
def operateur(a,b):
    op=input("Veuillez choisir l'opération + - * /: ")
    match op:
        case "+":
           print(a+b)
        case "-":
            print(a-b)
        case "*":
            print(a*b)
        case "/":
            print(a/b)
        case _:
            print("non valide")
            operateur(a,b)



a,b=valeur()
operateur(a,b)
decision=input("voulez vous arrêter?? o/n: ")
while decision != "o":
    a,b=valeur()
    operateur(a,b)
    decision=input("voulez vous arrêter?? o/n: ")
    
print("A la prochaine")

            
            

            

        

        
    