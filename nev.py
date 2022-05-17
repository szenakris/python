from opcode import hasnargs
from operator import truediv

""""
def nev(n):
    if n != 0:
        nev(n-1)
        print('Kristóf')
nev(100)
# ------------------------------------------------------------
def akóba_vált(liter):
    return liter/58.6

print('999 liter az', akóba_vált(999), 'akó.')
# ------------------------------------------------------------
def betűkkel(szám):
    számok_nevei = ['nulla', 'egy', 'kettő', 'három', 'négy', 'öt', 'hat', 'hét', 'nyolc', 'kilenc']
    return számok_nevei[szám]

for szám in range(10):
    print(szám, betűkkel(szám))
# ------------------------------------------------------------
szo = input ('kérem adjon meg egy szót')
def névelő(szó):
    magánhangzók = ['a', 'á','e','é','i', 'í', 'o', 'ó', 'ö', 'ő', 'u', 'ú', 'ü', 'ű']
    if szó[0] in  magánhangzók:
        return 'az'
    else:
        return 'a'
print(névelő(szo), szo)
# ------------------------------------------------------------
def hengrend(szó):
    mély_magánhangzók = ['a', 'á', 'o', 'ó', 'u', 'ú']
    magas_magánhangzók = ['e', 'é','i', 'í', 'ö', 'ő','ü', 'ű']
    volt_mély = False
    volt_magas = False
    for betű in szó:
        if betű in mély_magánhangzók:
            volt_mély = True
        elif betű in magas_magánhangzók:
            volt_magas = True
    if volt_mély and not volt_magas:
        return('mély')
    elif not volt_mély and volt_magas:
        return ('magas')
    elif volt_mély and volt_magas:
        return('vegyes')
    else:
        return('nincs magánhangzó a szóban')
    
szó = input('írj ide egy szót!')
print(hangrend(szó))
"""
# ------------------------------------------------------------
def monogram(név):
    szóköz = név.index(' ')
    return név[0]+ '. '+név[szóköz+1]+'.'

név = input('írd be a neved! ')
print(név, 'monogrammja:', monogram(név))

# ------------------------------------------------------------
