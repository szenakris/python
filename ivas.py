össz = 0 
while össz <= 35 and (ivás:=int(input('Hány decit ittál???'))):
    print(f'Már {(össz:=össz+ivás)/10:3.1f} litert ittál')
    if össz >= 25:
        print('már elérted a napi célt!')
print('béka nől a hasadba')
