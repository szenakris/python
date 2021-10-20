import random
honap = ['Január', 'Február', 'Március','Április', 'Május']
for i in honap:
    print(i, end=' ')
print('\nA tömb méret:', len(honap))
for j in range(len(honap)):
    print('%d. hónap: %s' % (j+1, honap[j]))
print(random.choice(honap))


strl = 'isz'
hb = ''
hb ='h' + strl + 'ed'
print(hb)
print(hb[3])
hb[0] = 'v'

strl = 'hiszed'
print(len(strl))
print(strl[1:4])
strl = strl[1:]

strl = strl[:3]+'o'+strl[4:]
print(strl)