class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary
       
    def showDetails(self):
        print("role=", self.role)    
        print("dept=", self.dept)
        print("salary=", self.salary)
        
class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "50000") 
        
#E1 = Employee("accountant", "Fianance", "40000")
#E1.showDetails()  
E2 = Engineer("FArhat", 49)
E2.showDetails()    