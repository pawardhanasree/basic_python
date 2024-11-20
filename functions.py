#function
def name(fname, lname):
    print("Hello!", fname, lname)

name("Dhana Sree", "Pawar")

#default arguments
print("\nDefault Arguments")
def name(fname = "Dhana Sree", lname = "Pawar"):
    print("Hello!", fname, lname)

name()
name("Gayathri")
name("Sanjay","Kumar")

#Keyword arguments
print("\nKeyword arguments")
def name(fname, lname):
    print("Hello!", fname, lname)

name(lname="Pawar", fname="Dhana Sree") 

#Required arguments
print("\nRequired arguments")
def name(fname, lname):
    print("Hello!", fname, lname)

name("Dhana Sree", "Pawar")

#Variable-length Arguments
print("\nVariable-length arguments")
def name(*names):
    print("Hello!", end = " ")
    for i in names:
        print(i, end=" ")

name("Dhana Sree", "Pawar")
name("James","Bruno", "Buchanan")

def average(*numbers):
    sum=0
    for num in numbers:
        sum = sum + num
    avg = sum / len(numbers)
    print("Average is :", avg )

average(3,5,7,8,9,1)

#Keyword arbitary arguments
print("\nKeyword arbitary arguments")
def name(**names):
    print("Hello!", end = " ")
    for i in names:
        print(names[i], end=" ")

name(fname = "Dhana Sree", laname = "Pawar")
name(fname = "James", mname = "Bruno", lname = "Buchanan")

#use of return statements
print("\nReturn statements")
def average(*numbers):
    sum=0
    for num in numbers:
        sum = sum + num
    avg = sum / len(numbers)
    return avg

print("Average is:", average(3,5,7,8,9,1))
