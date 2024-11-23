set1 = {"Pawar", 19, 0.87, True, 19}
print(set1)

#prints dictionary
set2 = {} #empty dictionary
print(type(set2))

#prints set  
set3 = set() #empty set
print(type(set3))

#Accessing the items in the set
for item in set1:
    print(item)

#union()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
print("Union:", cities1.union(cities2))

#union_update()
cities1.update(cities2)
print("Union_update:", cities1, cities2)

#intersection()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
print("Intersection:", cities1.intersection(cities2))

#intersection_update()
cities1.intersection_update(cities2)
print("Intersection_update:", cities1, cities2)

#symmetric_difference()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
print("Symmetric_difference:", cities1.symmetric_difference(cities2))

#symmetric_difference_update()
cities1.symmetric_difference_update(cities2)
print("symmetric_difference_update:", cities1, cities2)

#difference()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
print("Difference:", cities1.difference(cities2))

#difference_update()
cities1.difference_update(cities2)
print("Difference_update:", cities1, cities2)

#isdisjoint()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul","Kabul","Madrid"}
print("Disjoint:", cities1.isdisjoint(cities2))

cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Punjab", "Seoul","Kabul","Telangana"}
print("Disjoint:", cities1.isdisjoint(cities2))

#issuperset()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
cities3 = {"Delhi", "Tokyo"}
print("Superset:", cities1.issuperset(cities2))
print("Superset:", cities1.issuperset(cities3))

#issubset()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
cities3 = {"Delhi", "Tokyo"}
print("Subset:", cities1.issubset(cities2))
print("Subset:", cities3.issubset(cities1))


#add()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities1.add("Seoul")
print("Add:", cities1)

#remove()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities1.remove("Tokyo")
print("Removed Tokyo:", cities1)
#cities1.remove("Seoul") #Key error


#discard()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities1.discard("Tokyo")
print("Discarded Tokyo:", cities1)
cities1.discard("Seoul") #No error

#pop()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
item = cities1.pop()
print(cities1)
print(item)

#del()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
del cities1
#print(cities1) #name error

#clear()
cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
cities1.clear()
print(cities1)

cities1 = {"Tokyo", "Madrid","Berlin", "Delhi"}
if "Delhi" in cities1:
    print("Delhi is present")
else:
    print("Delhi is absent")
