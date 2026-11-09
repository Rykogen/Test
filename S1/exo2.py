a= int(input("Veuillez entrer le 1er nombre"))
b= int(input("Veuillez entrer le 2e nombre"))
print(f"SOmme: {a+b}")
print(a-b)
print(a*b)
if b==0:
    print("pas de quotient possible")
else:
    print(a/b)
    
    
print(a/b if b!=0 else "rien à faire")
    
