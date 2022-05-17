forrasfajl = open('raspberries.txt', 'w', Enconding = 'utf-8')
ripk = []
for sor in forrasfajl:
    ripk.append(sor.strip().split(';'))
forrasfajl.close()