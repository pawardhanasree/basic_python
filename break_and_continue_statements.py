#break
for i in range(1,101,1):
    print(i, end=" ")
    if(i == 50):
        break
    else:
        print("Mississippi")
print("Thank you!")

#continue
for i in [2,3,4,6,8,0]:
    if(i % 2 != 0):
        continue
    print(i)

#Example 2
print("Break statement")
for i in range(15):
    print("2 x", i+1, "=", 2 * (i+1))
    if (i == 11):
        print("loop breaks")
        break

print("Continue statement")
for i in range(15):
    print("2 x", i+1, "=", 2 * (i+1))
    if (i == 11):
        print("skips loop")
        continue