re = open ("adat.txt", 'r')
line = re.readline()
print(line)
re.close()

re = open ("adat.txt", 'r')
line = re.readline()
while line !="":
    line = line.strip()
    print(line)
    line = re.readline()
re.close()

#60
re = open ("adat.txt", 'r')
line = re.readline()
while line !="":
    line = line.strip()
    datas = line.split()
    print("%s/%s %s %s/%s=" %) \
        (datas [0], datas [1],
        datas [4], datas [2],
        datas[3],))
    line = re.readline()
re.close()

#61
need = []
re = open("igyeny.txt", 'r')
line = re.readline()
line = re.readline()
rn = int(re.readline())
for i in range (rn):
    line = re.readline()
    line= line.strip()
    need.append(line.split())
re.close
for i in range(rn-1,-1,-1):
    print("%s. csapat - -indul: %s. sint, erkezik: %s szint, %s óra %s perc %s mp" \
        %(need [i][3],need [i][4],need [i][5],need [i][0],need [i][1],need [i][2],))

#62
class Needs():
    pass
need = []
re = open("igeny.txt", 'r')
line = re.readline()
line = re.readline()
rn = int(re.readline())
for i in range(rn):
    line = re.readline()
    line = line.strip()
    datas = line.split()
    need.append(Needs())
    need[i].h = int(datas[0])
    need[i].min = int(datas[1])
    need[i].sec = int(datas[2])
    need[i].team = int(datas[3])
    need[i].start = int(datas[4])
    need[i].stop = int(datas[5])
re.close()
for i in range(rn-1,-1,-1):
    print("%s. csapat - -indul: %s. sint, erkezik: %s szint, %s óra %s perc %s mp" \
        % (need[i].team, need[i].start, need[i].stop, need[i].h, need[i].min, need[i].sec))

#63
class Needs():
    pass
need = []
re = open("igeny.txt", 'r')
line = re.readline()
line = re.readline()
rn = int(re.readline())
for i in range(rn):
    line = re.readline()
    line = line.strip()
    datas = line.split()
    need.append(Needs())
    need[i].h = int(datas[0])
    need[i].min = int(datas[1])
    need[i].sec = int(datas[2])
    need[i].team = int(datas[3])
    need[i].start = int(datas[4])
    need[i].stop = int(datas[5])
re.close()
for i in range(rn-1,-1,-1):
    print("%s. csapat - -indul: %s. sint, erkezik: %s szint, %s óra %s perc %s mp" \
        % (need[i].team, need[i].start, need[i].stop, need[i].h, need[i].min, need[i].sec))
