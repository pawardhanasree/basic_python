import time
time1 = time.strftime("%H:%M:%S")
print(time1)

if (time1 < "12:00:00"):
    print("Good Morning!!")
elif(time1 >= "12:00:00" and time1 < "17:00:00"):
    print("Good Afternoon!!")
else:
    print("Good Evening!!")