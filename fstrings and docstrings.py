#fstrings
name = "Dhana Sree"
country  = "India"
print(f"Hello, My name is {name} and I'm from {country}")

txt = "for only {price:.2f} dollars"
print(txt.format(price = 40))

#if we have to print {name} in output through fstrings
print(f"Hello, My name is {{name}} and I'm from {{country}}")

#docstrings
def square(n):
    '''Takes input number n and returns the square of the n'''
    return (n**2)

num1 = int(input("Enter a number: "))
print("Square of the number is :", square(num1))
print(square.__doc__) #displays docstring

#docstrings
def add(n1, n2):
    print(n1, n2)
    '''Takes input number n1 and n2 and returns the sum of those two numbers'''
    return (n1 + n2)

num1 = int(input("Enter a number1: "))
num2 = int(input("Enter a number2: "))
print("Sum of the numbers is :", add(num1, num2))
print(add.__doc__) #ouput is None as the first line of the function is not docstring

#Zen of Python
import this