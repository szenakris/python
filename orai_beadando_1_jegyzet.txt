#1
fruits = {"apple", "banana", "cherry"}

fruits.clear()

print(fruits)

#2
x = fruits.copy()

print(x)

#3
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)

#4
x.difference_update(y)

print(x)

#5
a = x.intersection(y)

print(a)
#Olyan halmazt ad, amely vissza adja mind két halmazban található elmeket.

#6
x.intersection_update(y)

print(x)

#7
b = x.isdisjoint(y)

print(b)
#Az isdisjoint() metódus igaz értéket ad vissza, ha egyik elem sem szerepel mindkét halmazban, ellenkező esetben False értéket ad 

#8
#Az issubset() metódus igaz értéket ad vissza, ha a halmaz összes eleme létezik a megadott halmazban, ellenkező esetben pedig hamis értéket ad vissza.
d = {"a", "b", "c"}
e = {"f", "e", "d", "c", "b", "a"}

c = d.issubset(e)

print(c)

#9
#Az issuperset() metódus True értéket ad vissza, ha a megadott halmaz összes eleme létezik az eredeti halmazban, ellenkező esetben pedig a False értéket adja vissza.
f = {"f", "e", "d", "c", "b", "a"}
g = {"a", "b", "c"}

e = f.issuperset(g)

print(e)

#10
#A symmetric_difference() metódus olyan halmazt ad vissza, amely mindkét halmaz összes elemét tartalmazza, de nem tartalmazza azokat, amelyek mindkét halmazban vannak.
i = {"apple", "banana", "cherry"}
j = {"google", "microsoft", "apple"}

h = i.symmetric_difference(j)

print(h)

#11

#pop()
#A pop() metódus eltávolít egy véletlenszerű elemet a halmazból.
fruits.pop()

print(fruits)

#remove()
#A remove() metódus eltávolítja a megadott elemet a halmazból.
fruits.remove("banana")

print(fruits)

#update()
#Az update() metódus frissíti az aktuális készletet egy másik halmazból (vagy bármely más iterálható) elemek hozzáadásával.
q = {"apple", "banana", "cherry"}
w = {"google", "microsoft", "apple"}

q.update(w)

print(q)