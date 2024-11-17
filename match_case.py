num1 = int(input("Enter a number: "))
# num1 is the variable to match
match num1:
    # if num1 is 0
    case 0:
        print("num1 is zero")
    # case with if-condition
    case 4 if num1 % 2 == 0:
        print("num1 % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if num1 < 10:
        print("num1 is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(num1)