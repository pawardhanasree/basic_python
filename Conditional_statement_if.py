#if statement
print("If statement")
num1 = int(input("Enter the number: "))
if (num1 >= 0):
    print("Number is positive") 

#if-else statment
print("If-else statement")
num1 = int(input("Enter the number: "))
if (num1 >= 0):
    print("Number is positive") 
else:
    print("Number is negative")

#if-elif-else statment
print("If-elif-else statement")
num1 = int(input("Enter the number: "))
if (num1 > 0):
    print("Number is positive") 
elif (num1 == 0):
    print("Number is zero")
else:
    print("Number is negative")

#Nested if-elif-else statemet
print(" Nested If-elif-else statement")
num1 = int(input("Enter the number: "))
if (num1 < 0):
    print("Number is negative")
elif (num1 > 0):
    if (num1 > 0 and num1 <= 10):
        print("Number is between 0-10")
    elif (num1 > 10 and num1 <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 30")
else:
    print("Number is zero")

#single hand if else
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))
print(num1) if num1 > num2 else print("Equal") if num1 == num2 else print(num2)