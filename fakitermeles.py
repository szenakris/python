import random

wr = open("fa.txt", "w")
fa = []
szam = 0
while szam != 31:
    kitermeles = random.randint(50,100)
    fa.append(kitermeles)
    szam += 1

ossz = 0
for megtermelt in fa:
    ossz += megtermelt
print(f'A márciusi összes fatermelés {ossz}')
wr.write(f'A márciusi összes fatermelés {ossz}')
""""
ossz = szum(fa)
"""

atlag = ossz/len(fa)
print(f'A márciusi kitermelt fák átlaga: {atlag}')
wr.write(f'A márciusi kitermelt fák átlaga: {atlag}')
legkissebb = min(fa)
legnagyobb = max(fa)
""""
for i in fa:
    if i < legkissebb:
        legkissebb = i
    elif i > legnagyobb:
        legnagyobb = i
"""

print(f'a legkissebb {legkissebb} volt, a legnagyobb{legnagyobb}')
wr.write(f'a legkissebb {legkissebb} volt, a legnagyobb{legnagyobb}')ű
if 40 in fa:
    print('volt ollyan nap, ahol 40 volt a kitermelt fa')
    wr.write('volt ollyan nap, ahol 40 volt a kitermelt fa')
else:
    print('nem volt olyan nap, amikor 40 volt a kitermelt fa')
    wr.write('nem volt olyan nap, amikor 40 volt a kitermelt fa')



van40= False
for x in fa:
    print('van ilyen')
    van40= True
    break
else:
    print('nincs ilyen')