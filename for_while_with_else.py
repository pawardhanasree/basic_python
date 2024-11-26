#for-else block
for i in range(5):
    print("Number {}".format(i+1))
else:
    print("for Else block")

#while-else block
i = 0
while (i < 5):
    print(i)
    i = i + 1
else:
    print("While else block")

#if we use the break statement in loops, else block will not execute
i = 0
while (i < 5):
    print(i)
    i = i + 1
    if i == 3:
        break
else:
    print("While else block")
