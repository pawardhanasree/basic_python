tuple1 = (1, 2, 3, 4, 5, 2, 4)
tuple2 = ("Red", 5, 7.94, True, 34)
print(tuple1)
print(tuple2)

tuple3 = ("Red", "Violet", "Blue", "Green")
print(tuple3)

#IndexTo check if an item is present in the list
if "Blue" in tuple3:
    print("Blue is present")
else:
    print("Blue is not present")

#Indexing
print("3rd index element is:", tuple3[3])
print("1st index element is:",tuple3[1])

#Range of Index
animals = ("cat","dog","mouse","pig","horse","donkey","goat","cow","buffalo")
print(animals[3:7])
print(animals[-7:-2])

#printing all the elements 
print(animals[:])

#printing all the elements from a given index till the end
print(animals[3:])
print(animals[-6:])

#printing all the elements from the start to the given index
print(animals[:5])
print(animals[:-4])

#printing alternate values
print(animals[::2])
print(animals[-8:-1:2])

#print 3rd consecutive elements
print(animals[::3])

#Tuple Methods
#count()
tuple4 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print("Count of 2 in tuple4:", tuple4.count(2))

#index()
print("Index of 2 in tuple4:", tuple4.index(2))

#Concatinating two tuples
countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "Sri lanka")
countries2 = ("Vietnam", "India", "China")
southEastASia = countries1 + countries2
print(southEastASia)

