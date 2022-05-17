auto = input('Egy autónév rendel!')

vegsebesseg = int(input('mennyivel megy ez a '+ auto +'?'))

orszag = input('Hol készült a ' + auto + '?')


mondat1 = orszag + 'Vidéken készült a ' + auto +', ami' + str(vegsebesseg) + ' km/h-val képes menni.'
print(mondat1)

mondat2 = '{} videkein kersztül a {}, ami {} kmh végsebességre képes.'.format(orszag, auto, vegsebesseg)
print(mondat2)


