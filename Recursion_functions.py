#factiorial
def factorial(num):
    if (num == 0 or num == 1):
        return 1
    else:
        return num * factorial(num-1)
    
num = int(input("Enter a number: "))
print(f"Factorial of {num} is:", factorial(num))


#fibonacci series
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

num = int(input("Enter a number: "))
print(f"Fibonacci of {num} is:", fibonacci(num))
print(f"Fibonacci Sequence of {num} is:")
i = 0
while (i <= num):
    print(fibonacci(i), end = " ")
    i  = i + 1
