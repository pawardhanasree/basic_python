#Iterating over a string
name = "Dhana Sree Pawar"
for character in name:
    print(character, end = ", ")
print("\n")

#Iterating over a list
colors = ["Red", "Blue", "Green", "Yellow"]
for color in colors:
    print(color)

#Using range() function to print a statement multiple times
for num in range(5):
    print(num, end = ", ")
print("\n")

#Using range() function between range
for num in range(1, 10):
    print(num, end = ", ")
print("\n")

#Using range() function with range and step
for num in range(1, 20, 3):
    print(num, end=", ")
print("\n")