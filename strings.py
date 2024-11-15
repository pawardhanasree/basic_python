name = "Dhana Sree"
print("Hello,", name)

#To print double quotes inside the string, we can enclose it in single quotes
print('My name is "Dhana Sree Pawar"')

#Multiline strings can be written in three single / double quotes
str1 = '''I have started learning Python Programming.
This is the example of Multiline string.'''
print(str1)

#we can access the characters in a string
print(name[4]) #displays fouth character starting from zero
print(name[7])

#we can use loops to print every charcter of string 
for character in str1:
    print(character)

#To find the length of the string
print("Length of name is",len(name))
print("Length of str1 is",len(str1))

#Slicing of the string
#display characters from starting to end-1
print(name[:])
print(name[0:])
#All the ab0ve statement have the same output 

print(name[0:5])
print(name[6:11])
print(name[3:8])

#Negative indexing
#it's length of the string minus the negative index value
print(name[0:-5]) #print(name[0:len(name)-5])
print(name[-1:-2]) #displays blank if starting index is -1 
print(name[9:8]) #because indexing doesn't allow from last to first
print(name[-3:-1])