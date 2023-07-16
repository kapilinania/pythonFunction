# a={}   for a empty dictionary  use this one
# print(a,type(a))
# b=set()    for a empty set use this one
# print(b,type(b))

dict1 = {"kapil": "this is a boy", "koala": "this is a girl", "1": "number one"}
print(dict1["kapil"])
marks = {"kapil": 78, "raju": 45, "karan": 88}
print(marks["karan"])
# marks["kunal"]=85  here we can add another person
# print(marks.get("komal"))   none come here
# print((marks).get("kapil"))
print(marks.keys())
print(marks.values())
print(marks.items())
print(marks.clear())

print(marks)