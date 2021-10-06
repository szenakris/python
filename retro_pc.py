nev = input ('Mi a gép neve?')

mukodik = True if input('Működik (i/n)?') == 'i'else False

ar = int(input('Mennyibe kerül?'))

if (nev == 'ZX Spectrum' or nev == 'C64') and mukodik and ar <= 25000:
    print('zuráááásss')
else:
    print('hahaha... erre nincs pénzed!!')

    