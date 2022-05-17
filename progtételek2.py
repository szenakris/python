"""
*Egy sorozathoz egy értéket rendelő algoritmusok​
    Sorozatszámítás​
        Összegzés​
        Szorzás​
        Összefűzés​
    Eldöntés​
    Kiválasztás​
    Lineáris keresés​
    Megszámlálás​
    Maximum kiválasztás​
    Minimum kiválasztás​
*Egy sorozathoz egy sorozatot rendelő algoritmusok​
*Több sorozathoz egy sorozatot rendelő algoritmusok​
*Egy sorozathoz több sorozatot rendelő algoritmusok​
https://szit.hu/doku.php?id=oktatas:programozas:programozasi_tetelek:python_megvalositas
"""


#Összegzés - összeadás
t = [ 3, 8, 2, 4, 5, 1, 6]
 
osszeg = 0
for num in t:
    osszeg = osszeg + num
 
print("Összeg: ", osszeg)
#print(f' összeg egyenlő {sum(t)}')


#Összegzés - szorzás
osszeg = 1
for num in t:
    osszeg = osszeg * num
 
print("Összeg: ", osszeg)

#Összegzés - konkatenáció
osszeg = ''
for num in t:
    osszeg = str(osszeg) + str(num)
 
print("Összeg: ", osszeg)




#Megoldás
összes = 0
for bevétel in bevételek:
    #összes += bevétel #vagy:
    összes = összes + bevétel
    print('Napi bevétel:', összes, 'picula.')

összes = sum(bevételek)
print('Napi bevétel:', összes, 'picula.')


#Megszámolás - t = [ 3, 8, 2, 4, 5, 1, 6]
count = 0
for num in t:
    if num > 5:
        count = count + 1
 
print("5-nél nagyobb: ", count)

#Eldöntés - t = [ 3, 8, 2, 4, 5, 1, 6]
n = len(t)
#ker = int(input('Kérem adja meg a keresett számot')
ker = 5
 
i = 0
while i < n and t[i] != ker:
    i = i + 1
 
if i<n:
    print("Van ilyen: ", ker)
else:
    print("Nincs ilyen elem: ", ker)


        
 #Emlékszik?
 for i in range(-1, -11, -1): #ugye figyelsz a -11-re a -10 helyett?!
    print(i**3)



#Feladat
#Kérjünk be a felhasználótól egy szót, és döntsük el, hogy tartalmaz-e magán-hangzót.
#Amennyiben tartalmaz, írjuk ki, hogy "Van benne magánhangzó.". Ha nincs, akkor írjuk ki, hogy "Nincs benne magánhangzó" A begépelendő szóról feltételezhetjük, hogy csak az angol ábécé kisbetűit tartalmazza.
word = input("Kérek egy szót: ")
vowels = "aeiou"
n = len(word)
i = 0    
while i < n and vowels.find(word[i]) > -1:
    i += 1
if i >= n:
    print("Nincs benne magánhangzó.")
else:
    print("Van benne magánhangzó")




#Kiválasztást - t = [ 3, 8, 2, 4, 5, 1, 6]
n = len(t)
ker = 5
 
i = 0
while t[i] != ker:
    i = i + 1
 
print("Hányadik helyen van: ", i+1)


#Szélső értékek
# Maximun kiválasztás t = [ 5, 3, 6, 2, 1 ]
 
maxElem = t[0]
for elem in t:
    if elem > maxElem:
        maxElem = elem
print(maxElem)

# Minumum kiválasztás t = [ 5, 3, 6, 2, 1 ]
minElem = t[0]
for elem in t:
    if elem < minElem:
        minElem = elem
print(minElem)
