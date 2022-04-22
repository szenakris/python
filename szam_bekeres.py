def nem()

def pozneg(szam1):
    if szam1 >0:
        print(szam1, 'pozitív')
    elif szam1 < 0:
        print(szam1, 'negatív')
    else:
        print('nulla')

szam1 = None
while szam1 != '':
 szam1 = input('Írj ide egy számot! ')
 if szam1 != '':
        szam1 = float(szam1)
 pozneg(szam1)

szam1 = int(input('adja meg a számot'))    
while szam1 != ' ':
    szam1 = input('írj ide egy számot')
