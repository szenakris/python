import random

tömegek = []
for _ in range(20):
    tömegek.append(random.randit(1000,10000))
print(tömegek)

volt_nehez = False
nehez_szama =0
ossztomeg =0
nehezek_ossztomeg =0
for tömeg in tömegek:
    ossztomeg = ossztomeg + tömeg
    if tömeg > 9300:
        volt_nehez = True
        nehez_szama +=1
        nehezek_ossztomeg +
if volt_nehez:
    print('volt 9300 kilonál nehezebb jármű!')