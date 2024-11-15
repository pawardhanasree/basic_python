#To perform operation, both the variables should be of same datatype, if not we have to do typecasting

#Explicit typecasting
num1 = "45"
num2 = 9
print("Type of num1 is", type(num1))
print("Type of num2 is", type(num2))
# print(num1+num2) Typeerror: as two variables are of different datatypes
#The below command converts the num1 from str data type to int and performs the operation
print(int(num1) + num2)
print("Type of output is", type(int(num1) + num2))

#Implicit Typecasting
num3 = 45
num4 = 9.0 
print("Type of num3 is", type(num3))
print("Type of num4 is", type(num4))
#As num3 is int and num4 is float, the operation is performed 
#because python interpretor has converted num3 to float
print(num3 + num4)
print("Type of output is", type(num3 + num4))