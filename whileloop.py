#while loop

i = 1
while i <= 10:
    print(i)
    i += 1
print("program done ...")

# while True:
#     print("Program not done never")   while infinite loop

while True:
    num = int(input("Enter a NUmber ="))
    print(num)
    if num == 4:
        print("Loop Break")
        break
    elif num ==5:
        print("loop continue")
        continue

    else:
        print("wow number is here")