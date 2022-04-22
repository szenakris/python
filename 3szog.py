import math



a = int(input('adja meg az egyik oldalt'))
b = int(input('adja meg a másik oldalt'))
c = int(input('adja meg a harmadikoldalt'))
s = (a+b+c)/2
elsohszog = math.sqrt(s*(s-a)+(s-b)+(s-c))

a1 = int(input('első oldal'))
b1 = int(input('második oldal'))
c1 = int(input('harmadik oldal'))
s1 = (a1+b1+c1)/2
mashszog = math.sqrt(s1*(s1-a1)+(s1-b1)+(s1-c1))

if elsohszog > mashszog:
    print('első nagyobb')
elif elsohszog < mashszog:
    print('második nagyobb')
else:
    print('egyenlo')