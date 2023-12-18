from employee import Employee

class company:
    def __init__(self) :
        self.employees=[]

    def addemployee(self,newemployee):
        self.employees.append(newemployee)
    
    def displayemployee(self):
        print('curent employees:')
        for i in self.employees:
            print(i.firstname,i.lastname)
        print("----------------------------")

    def payemployee(self):
        print('paying employees:')
        for j in self.employees:
            print('paycheck for',j.firstname,j.lastname)
            print(f'amount ${j.paycheck():,.2f}')
            print("----------------------------")

    
def main():
    mycompany=company()

    employee1=Employee('leasha','krish',50000)
    mycompany.addemployee(employee1)
    
    employee2=Employee('nithya','krish',200000)
    mycompany.addemployee(employee2)

    mycompany.displayemployee()
    mycompany.payemployee()

main()