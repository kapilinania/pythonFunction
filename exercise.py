# Write a Python function that takes two numbers as input and returns their sum. Add comments to explain what each
# part of the function does.

def add_number(a, b):
    # here i am take two variable a and b
    c = a + b
    print(f" print {a}  and {b}", c)  # Print the value of c before returning
    return c


add_number(10, 30)


# set a and b value

# Write a Python program to check if a given number is even or odd.

def check_num(a):
    if a % 2 == 0:
        print("this is even number")
    else:
        print("this is odd number")


check_num(50)


# Write a Python program to find the factorial of a given number using recursion

def feactorial_num(a):
    if a == 1:
        return 1
    else:
        c = a * feactorial_num(a - 1)
        return c


res = feactorial_num(5)
print(f"factorial is= ",res)

# Function to find the largest element in a list

def find_largest_number(lst):
    largest = lst[0]
    for num in  lst:
        if num > largest:
            largest = num
    return largest
numbers = [10,0,4,50,99,45,12]
print(f"the largest number is {find_largest_number(numbers)}")
