OLVADASI_PONT = 1539
FORRAS_PONT = 2750

hofok = int(input('mekkora a hőfok?: '))
 if hofok < OLVADASI_PONT:
     print('Szilárd!')
elif hofok < FORRAS_PONT:
    print('Folyékony!')
else:
    print('Gáz!')