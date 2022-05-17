#írás
wr=open('10b.txt', "w")
wr.write('10b')
wr.close()
#olvasás
wr=open('10b.txt', "r")
tartalom = wr.read()
print(tartalom)


#kontextusok
with open ('10b', "r", encoding="utf-8") as file:
    file.write('10b')
#------------------------------------------------------

with open("10.b", "r", encoding="utf-8")

#------------------------------------------------------

wr=open('10.txt',"a")
wr.write('SZBJ')
wr.close()
