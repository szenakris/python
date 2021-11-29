import random

szam  = random.randrange(10,50)
szam2 = random.randrange(10)
lista1 = [szam,szam2]
lista2 = []
for i in lista1:
    print(i)
print('for ciklus')
print(szam)
print(szam2)

if szam < szam2:
    osztas1 = szam/szam2
    osztas2 = szam%szam2
    osztas3 = szam//szam2
    print(osztas1)
    print(osztas2)
    print(osztas3)
else:
    a = (szam2/szam)
    b = (szam2%szam)
    c= (szam2//szam)

lista2.append(a)
lista2.append(b)
lista2.append(c)
lista2.sort()

