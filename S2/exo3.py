def calcul(a,b):
    somme = a+b
    difference = a-b
    produit= a*b
    quotient= a/b if b!=0 else "division impossible"
    return somme,difference,produit,quotient



s,d,p,q= calcul(3,9)
print("Somme",s,"différence",d,"produit",p,"quotient",q)    