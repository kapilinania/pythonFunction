# Here I am store data in the file
a = "kapil is from India At jodhpur ohh"
# open("file name", "3 type read write or append mode")
# writing a file
# short way
# with open("test.txt", "w") as f:
#     f.write(a)

# long way
# fp =open("test.txt", "w")
# fp.write(a)
# fp.close()

# Reading a file
# short way
# with open("test.txt", "r") as f:
#     a = f.read()
#     print(a)

# long way
# fp =open("test.txt", "r")
# a = fp.read()
# print(a)
# fp.close()

# appending a file  at the end of the is appending the data
# short way
# with open("test.txt", "a") as f:
#     f.write("hellotask ")

# long way
fp =open("test.txt", "a")
fp.write(a)
fp.close()