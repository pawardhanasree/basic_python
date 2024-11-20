list1 = ["cat","dog","mouse","pig","horse","donkey","goat","cow","buffalo"]
list2 = [2,4,5,6,3,6,2,1,4,2,1,3,9,5,3]

#sort()
list1.sort()
list2.sort()
print("Ascending order:", list1)
print("Ascending order:", list2)

#descending order
list1.sort(reverse = True)
list2.sort(reverse = True)
print("Descending order:", list1)
print("Descending order:", list2)

#reverse
list1 = ["cat","dog","mouse","pig","horse","donkey","goat","cow","buffalo"]
list2 = [2,4,5,6,3,6,2,1,4,2,1,3,9,5,3]
list1.reverse()
list2.reverse()
print("Reverse of list1:", list1)
print("Reverse of list2:", list2)

#index()
list1 = ["cat","dog","mouse","pig","horse","donkey","goat","cow","buffalo"]
list2 = [2,4,5,6,3,6,2,1,4,2,1,3,9,5,3]
print("Index of mouse:",list1.index("mouse"))
print("Index of 3:", list2.index(3))

#count()
print("Count of 2:", list2.count(2))

#copy()
list3 = list1.copy()
print("Copy of list1", list3)

#append
list1.append("Rabbit")
print("Append the rabbit in list1:", list1)

#extend()
colors1 = ["violet","indigo","blue"]
colors2 = ["red", "green", "yellow", "orange"]
colors1.extend(colors2)
print("Extended the color2 in colors1:")
print("colors1:", colors1)
print("colors2:", colors2)

#Concatenating two string
colors1 = ["violet","indigo","blue"]
colors2 = ["red", "green", "yellow", "orange"]
print("concatenating two lists:", colors1 + colors2)

#pop()
colors1 = ["violet","indigo","blue", "green"]
colors1.pop()
print("Pop function:", colors1)
colors1.pop(1)
print("Pop function with parameter as 1:", colors1)