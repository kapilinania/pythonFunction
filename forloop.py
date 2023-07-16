# for loop
for i in range(5):
    print(i + 1)
print("print here....")
a = [1, 2, 3, 4, 5, 6]
# b = {2, 4, 5, 102, 100, 455}  set is not maintain order
for item in a:
    print(item)

# break and continue
print("break and continue is here")
for i in range(10):
    if i == 5:
        continue
        print(i)
    elif i== 8:
        break
        print(i)
    else:
        print(i)

