class Person:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
#derived class
class Employee(Person):
    def __init__(self,name,age,employee_id):
        super().__init__(name,age)
        self.employee_id=employee_id
emp=Employee("Bhavani",20,"Emp425")
print("Employee Details")
print("Name:",emp.name)
print("Age:",emp.age)
print("Employee-id",emp.employee_id)

