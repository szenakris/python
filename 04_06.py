hegym1 = int(input('adja meg az első hegy magasságát'))
hegym2 = int(input('adja meg az második hegy magasságát'))
if hegym1>hegym2:
    print(f'az első hegy {hegym1} magasabb, mint a második{hegym2}')
elif hegym2>hegym1:
    print(f'az első hegy {hegym1} kisebb, mint a második{hegym2}')
else:
    print('a két hegy egyenlő magasságú')

def magas(m):
    return m/1000

def nevelo(hegymaszo_nev):
    mgh = 'aáeéiíoóöőuúüű'
    if hegymaszo_nev[0] in mgh.lower():
        return "AZ"
    else:
        return 'A'

def nagybetu(hegymaszo_nev):
    return hegymaszo_nev.upper()                                                                                                                                                                                                                                                                                                                                                                                                                            


for _ in range(3):
    hegymaszo_nev = input('adja meg a hegymászó nevét!')
    m = int(input('Adja meg a hegy magasságát!'))
    valtas = float(magas(m))
print(f'A {hegymaszo_nev} nevű hegymászó {valtas}km magasra jutott feeeeefeleeee')

class Szuperhos:
    def __init__(self, nev, szuperero):
        self.nev = nev                  #https://okt.sed.hu/szkriptnyelvek/gyakorlat/python/object/
        self.szuperero = szuperero