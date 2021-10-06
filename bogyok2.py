nev =input('Mi a neve')

bogyo = int(input ('Hány darabot gyűjtöttél'))

if bogyo < 10:
    minősíés = 'zsenge'
if bogyo > 20:
    minősítés = 'Nagy koponya'
else: bogyo < 20:
    minősítés = 'gyűjtögető'

print(f'{nev} egy {minősítés}')

    
