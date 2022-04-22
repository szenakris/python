import math

haromszog = [3,4,5]
print(haromszog)
kerület = 0
for i in haromszog:
    kerület = kerület + i
    print(kerület)

kerület= sum(haromszog)
print(kerület)

s = kerület/2
terület = s * math.sqrt((s-haromszog[0])* (s-haromszog[1])* (s-haromszog[2]))
print(f'A haromszognek a területe : {terület}')

wr = open("haromszog.txt", 'w')
wr.write(f'A haromszognek a területe : {terület}')
wr.close()

# haromszog = [3,4,5]
wr = open('haromszog.txt', 'a')
keres = int(input("addjon meg egy számot"))
vanilyen = None
# a = len(haromszog)
for index in range(len(haromszog)):
    if haromszog[index] == keres:
        vanilyen = True
        holvan = index
        break
if vanilyen:
    print( f' sorszáma , {holvan +1}')
    wr.write(f'\nsorszáma {holvan +1}')
else:
    print(f'nincs')
    wr.write(f'\nnincs')

if keres in haromszog:
    print(f'a kersett szám sorszáma {haromszog.index(keres)+ 1}')
    wr.write(f'\na kersett szám sorszáma {haromszog.index(keres)+ 1}')
else:
    print (f'nincs')
    wr.write(f'\nnincs')


# haromszog = [3,4,5]
max = haromszog[0]
for oldal in haromszog:
    if oldal > max:
        max = oldal
print(f'a legnagyibb oldal mérete: {max}')        
wr.write(f'\na legnagyibb oldal mérete: {max}')



# haromszog = [3,4,5]
min = haromszog[0]
for oldal in haromszog:
    if oldal < min:
        min = oldal
print(f'a legkisebb oldal mérete: {min}')        
wr.write(f'\na legkisebb oldal mérete: {min}')


wr.close()