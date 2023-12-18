from employee import Employee

class company:
    def __init__(self) :
        self.employees=[]

    def addemployee(self,newemployee):
        self.employees.append(newemployee)
    
    def displayemployee(self):
        print('curent employees:')
        for i in self.employees:
            print(i.fname,i.lastname)
        print("----------------------------")


    
def main():
    print("hello")
    mycompany=company()

    employee1=Employee('leasha','krish',50000)
    mycompany.addemployee(employee1)
    
    employee2=Employee('nithya','krish',200000)
    mycompany.addemployee(employee2)

    print(mycompany.displayemployee)

main()