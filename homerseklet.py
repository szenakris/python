import numbers
def homerseklet(hom):
    hom = [9,-16,-19,-8,-2,14,15,16,-8,8,-3,-9,-4,-3,18,-17,-7,-1,7,10,-12,14,7,6,-6,-20,10,3]
    hom1 = hom.count(numbers)
    if hom1[0] in hom:
        return 'igaz'
    else:
        return 'hamis'
print(homerseklet(hom))

wr = open("hom.txt", 'a')
wr.write("")
wr.close()
wr = open("hom.txt", "r")
print(wr.read())