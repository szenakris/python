from fileinput import close


class allatfaj:
    def __init__(self, fajnev, tomeg):
        self.fajnnev = fajnev
        self.tomeg = tomeg
#kérej be 3 faj nevét és tömergét és ezt add hozzá egy listához

#bekérés
#for_ in range(3)
allat1 = input('adjon meg egy állatot')
tomeg1 = int(input('mekkora a tömege?'))

allat2 = input('adjon meg egy állatot')
tomeg2 = int(input('mekkora a tömege?')) 

allat3 = input('adjon meg egy állatot')
tomeg3 = int(input('mekkora a tömege?'))  
#lsita
nev_lista = []
tomeg_lista = []

nev_lista.append(allat1)
nev_lista.append(allat2)
nev_lista.append(allat3)

tomeg_lista.append (tomeg1)
tomeg_lista.append (tomeg2)
tomeg_lista.append (tomeg3)

print(nev_lista)
print(tomeg_lista)
#mekkkora a legnehezebb?
legnehezebb_allat = tomeg_lista
max_tomeg = None
for max in tomeg_lista:
    if max_tomeg is None or max > max_tomeg):
        max_tomeg = max
print('ez a max:', max_tomeg)
#fájl írás
# wr = open('legnehezebb.txt', 'w'´)
# wr.write(legnehezebb_allat)
# wr.close

# lezárás