import re
n=input("Veuillez entrer un numero de telephone: ")
if (re.match(r"\s*(0|\+33)\s*[1-9](\s*\d){8}\s*$",n)) is not None:
    print(re.sub(r"\s*","",n),"est valide")
else:
    print(re.sub(r"\s*","",n), "n'est pas valide")