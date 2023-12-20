class Employee:
    def __init__(self,firstname,lastname,salary) :
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary
    
    def paycheck(self):        # salary is split evenly by 52 weeks in a year -->      (365/7)=52
        return self.salary/52
    
# employee15=Employee('leasha','krish',50000)
# print(employee15.firstname)
# print(employee15.lastname)
# print(employee15.paycheck())
    
# to print the float value in two decimal places
# print(f'{employee15.paycheck():,.2f}')
