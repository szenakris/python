egyik = int(input('Ajon meg egy számot '))
masik = int(input('Ajon meg egy masik számot '))
jel = input('Ajon meg egy műveleti jelet')

print('A művelet eredménye:', end =' ')
if jel == '+':
    print(egyik+masik)

elif jel == '-':
    print(egyik-masik)

elif jel == '%':
    print(egyik%masik)

elif jel == '/':
    print(egyik/masik)

elif jel == '>>':
    print(egyik>>masik)

