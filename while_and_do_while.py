#while loop
num1 = int(input("Enter a number1: "))

while num1 <= 5:
    print(num1, end = ", ")
    num1 = num1 + 1

#while loop with an else block
num2 = int(input("\nEnter a number2: "))

while num2 <= 5:
    print(num2, end = ", ")
    num2 = num2 + 1
else:
    print("Number is greater than 5")


#do...while loop
num3 = int(input("\nEnter a number3: "))

while True:
    print(num3, end = ', ')
    num3 = num3 - 1
    if (num3 < 0):
        break
    