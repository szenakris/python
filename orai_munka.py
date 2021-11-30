import random

szam1 =  int(input('kérem adjon meg egy számot!'))
szam2 = random.randint(10, 50)

print(szam1)
print(szam2)

SZAM3 = 5

szamok = []

szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)

print(szamok)

if szam1 % 2 == 0:
    print('a szám páros')
else:
    print('a szám páratlan') 

nev = input("kérem adja meg a nevét")

szamok2 = {}
szamok2.add(szam1) 
szamok2.add(szam2) 
szamok2.add(SZAM3) 
my_list = [1,2,3,4,5,"abc"]
with open('your_file.txt', 'w') as file:
    for item in my_list:
        file.write("%s\n" % item )


f = open ('your_file.txt')
tartalom = f.read()
print(tartalom)
close()