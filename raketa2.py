import time

ido = int(input("Mennyi idő legyen a kilövésig?"))
while ido > 0:
        print (ido),
        time.sleep(1),
        ido -=1
felfuggesztes = input("felfüggeszted? igen/nem")
if felfuggesztes == "igen":
    ido += 1
    print("felfüggesztve")
elif felfuggesztes == "nem":
    ido += 0
    print ("Kilövés!!!") 


