nev = input('kérem adja meg a nevét! ')

bogyo = int(input('hány bogyód van?'))

if bogyo < 10:
    minősítés = 'zsenge'
elif bogyo > 20:
    minősítés = 'gyűjtögető'

print(f'{nev} egy {minősítés}.')