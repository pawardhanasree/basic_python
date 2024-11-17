num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
operator = input("Enter an operator: ")

match operator:
    case "+" :
        print(num1 + num2)
    case "-" :
        print(num1 - num2)
    case "*" :
        print(num1 * num2)
    case "/" :
        print(num1 / num2)
    case "%" :
        print(num1 % num2)
    case _ :
        print("Invalid operator")

