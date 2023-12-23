from  Emplo import employee,salaryemp,houremp,commissionemp

class company:
    def __init__(self):
        self.employees=[]

    def add_emp(self,newemp):
        self.employees.append(newemp)

    def display_emp(self):
        print("current employees: ")
        for i in self.employees:
            print(i.fname,i.lname)
        print("------------------------------")

    def pay_emp(self):
        print("paying employees: ")
        for i in self.employees:
            print("paycheck for: ",i.fname,i.lname)
            print(f'amount: {i.calpaycheck():,.2f}')
            print("--------------------------")


def main():
    mycompany=company()

    employee1=salaryemp('leasha','krish',25000)
    mycompany.add_emp(employee1)
    employee2=houremp('nithya','krish',25,50)
    mycompany.add_emp(employee2)
    employee3=commissionemp('nimalini','krish',30000,5,200)
    mycompany.add_emp(employee3)

    mycompany.display_emp()
    mycompany.pay_emp()

main()