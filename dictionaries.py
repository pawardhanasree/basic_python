info = {"name":"Gayathri", "age":21,"eligible":True}
print(info)

empty_dict = {}
print(empty_dict)
print(type(empty_dict))

#accessing single value
print(info["name"]) #using square brackets
print(info.get("name")) #using get() method

#print(info["DOB"]) #Keyerror
print(info.get("DOB")) #prints NULL

#Accessing multiple values
print(info.values())

#Accessing Key values
print(info.keys())

#Accessing items (key-value pairs)
print(info.items())

#we can access the key, values using for loop
print("Values")
for key in info.keys():
    print(info[key])

for values in info.values():
    print(values)

print("Keys")
for key in info.keys():
    print(key)

print("Key value pairs")
for key, value in info.items():
    print(key, value)

#dictionary methods
#update()
info = {"name":"Gayathri", "age":21,"eligible":True}
info.update({"age":22})
info.update({"DOB":2003})
print(info)

#pop()
info.pop("DOB")
print(info)

#info.pop("DATE") #KeyError

#popitem()
info.popitem()
print(info)

#del
del info["age"]
print(info)

#del info["DOB"] #KeyError

#clear()
info.clear()
print(info)

#del
del info
#print(info) #NameError