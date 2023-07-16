# class employee:
#     salary=45000
#     name="kapil"
#     def getsalary(self):
#         return self.salary
# kapil=employee()
# print(kapil.salary)
# print(kapil.name)

class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        print(self.salary)

kapil = employee("kapil", 55000)
# print(kapil.salary)
# print(kapil.name)
kapil.getsalary()



