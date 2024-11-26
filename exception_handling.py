try:
    num = int(input("Enter an integer:"))
except ValueError:
    print("Number entered is not an integer")

#try with multiple except blocks
try:
    num = int(input("Enter an integer:"))
    a = [3,5,6]
    print(num, a[num])
except ValueError:
     print("Number entered is not an integer")
except IndexError:
    print("Index is out of range")

#try...except...else...finally blocks
try:
    num = int(input("Enter an integer:"))
    a = [3,5,6]
except ValueError:
     print("Number entered is not an integer")
except IndexError:
    print("Index is out of range")
else:
    print(num, a[num])
finally:
    print("This block is always executed")
