# kiválasztás
t = [3, 8 ,2, 4, 5, 1, 6]

n = len(t)
ker = 5

i= 0
while t[i] != ker:
    i = i +1
print("hanyadik helyen van:",i+1)

# Lineáris keresés
t = [3, 8 ,2, 4, 5, 1, 6]

n = len(t)
ker = 5

i= 0
while i < n  and t[i] != ker:
    i = i + 1
if (i < n):
    print('van'+str(ker)+ 'elem')
    print('helye:', i + 1)
else:
    print('nincs'+ str(ker)+'elem')

# másolás
a = [3, 8, 2, 4, 5, 1, 6]
b = []

def dupla(num):
    return num*2

for elem in a:
    b.append(dupla(elem))

# kiválogatás
a = [3, 8, 2, 4, 5, 1, 6]
b = []
fror elem in a:
if elem < 5:
    b.append(elem)
print(b)

