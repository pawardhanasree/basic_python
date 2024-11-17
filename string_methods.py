str1 = "AbcD efgHij"
print("Upper:", str1.upper())
print("Lower:", str1.lower())
print("Capitalize:", str1.capitalize())
print("Title:", str1.title())
print("Swapcase:", str1.swapcase())

str2 = "   Silver Spoon  "
print("Strip:", str2.strip())

str3 = "!!!Hello!!!"
print("Rstrip:", str3.rstrip("!"))
print("Lstrip:", str3.lstrip("!"))
print("Strip!:", str3.strip("!"))

str4 = "Silver Spoon"
print("Replace:", str4.replace("Sp", "M"))
print("Split:", str4.split(" "))
print("Center:", str4.center(60))
print("Center with characters:", str4.center(60,"~"))
#print(len(str4))
#print(len(str4.center(60)))

str5 = "Welcome to the console!!!"
print("Count:", str5.count("o"))
print("Endswith:", str5.endswith("!!"))
print("Endswith between string:", str5.endswith("to", 4,10))
print("Endswith False example:", str5.endswith("le"))
print("Startswith:",str5.startswith("Wel"))

str6 = "He is Dan, he is an honest man"
print("Find:", str6.find("is"))
print("Find False example:", str6.find("Daniel"))
print("Index:", str6.index("is"))
#print(str6.index("Daniel")) #ValueError: substring not found

str7 = "WelcomeToTheConsole01"
print("Isalnum:", str7.isalnum())
print("Isalnum False example:", str5.isalnum())

str8 = "WelcomeToTheConsole"
print("Isalpha:", str7.isalpha())
print("Isalpha False example:", str5.isalpha())

str9 = "hello world!"
print("Islower:", str9.islower())

str10 = "HELLO WORLD!"
print("Isupper:", str10.isupper())
print("Istitle:", str10.istitle())

str11 ="Welcome\n"
print("Isprintable false example:", str11.isprintable())
print("Isprintable:", str5.isprintable())

str12 = "     "
print("Isspace: ", str12.isspace())