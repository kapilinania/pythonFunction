name = "kapil*12"
print(name)
num1 = 'single quotes'
print(num1)
# string slice
print(name[0:3])  # 0 1 2 ( 0 include and 3 is excluded)
print(name[3:5])
print(name.upper())
print(name.capitalize())
print(name.count("i"))  # this function show how many times come in words your character
print(name.isalnum())  # give word not alphanumeric word
num = "785496"
print(num.isnumeric())
print(name.isnumeric())

# string types
# use \ for join string inside string
a = 'kapil inania' \
    ' wow this is great'
b = "kapil inania second"
# this is a right way to write multi line string
c = '''kapil inaniya three   
and he is from jodhpur       .  wow       it is awesome
'''
print(a, b, c)
