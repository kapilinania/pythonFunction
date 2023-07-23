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
print(f"factorial is= ", res)


# Function to find the largest element in a list

def find_largest_number(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest


numbers = [10, 0, 4, 50, 99, 45, 12]
print(f"the largest number is {find_largest_number(numbers)}")

""" here  we are learn some variable example"""


# Write a Python program that swaps the values of two variables a and b without using a temporary variable.

def swap_data(a, b):
    print(f"Before swap a = {a} and b = {b}")
    a, b = b, a
    print(f"After swap a = {a}, and b = {b}")


swap_data(10, 20)


# Write a Python function that takes a list of numbers as input and returns the sum and average of the numbers as a
# tuple.
def task(number):
    data = sum(numbers)
    return data


numbers = [10, 20, 30, 40, 50]
data = sum(numbers) / len(numbers)
print(f"sum of list is = ", data)

# Write a Python program that prompts the user to enter their name and age.
# Then, print a message saying, "Hello, {name}! You are {age} years old."

a = input("enter your age:")
b = input("Enter Your name:")
print("Your age is", a)
print("Your name is", b)


# is here
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


celsius_to_fahrenheit(50)
fahrenheit_to_celsius(100)
