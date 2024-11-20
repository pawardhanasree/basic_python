list1 = ["Red", "Violet", "Blue", "Green"]
print(list1)

#IndexTo check if an item is present in the list
if "Blue" in list1:
    print("Blue is present")
else:
    print("Blue is not present")

#Indexing
print("3rd index element is:", list1[3])
print("1st index element is:",list1[1])

#Range of Index
animals = ["cat","dog","mouse","pig","horse","donkey","goat","cow","buffalo"]
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


