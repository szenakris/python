#JELSZO = input('Adjon meg egy jelszót!')
#print(JELSZO)
JELSZO = 'jelszó'
jelszo = None
while jelszo != JELSZO:
    jelszo = input('Adjon meg egy jelszót!')
    if jelszo != JELSZO:
        print('nem ez a jelszava!')
        pass
print('ügyes vagy!')
