class employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname


class salaryemp(employee):
    def __init__(self, fname, lname,salary):
        super().__init__(fname, lname)
        self.salary=salary

    def calpaycheck(self):
        return self.salary/52
    
class houremp(employee):
    def __init__(self, fname, lname,weekly_hours,hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours=weekly_hours
        self.hourly_rate=hourly_rate

    def calpaycheck(self):
        return  self.weekly_hours*self.hourly_rate
    

class commissionemp(salaryemp):
    def __init__(self, fname, lname, salary,salesnum,comrate):
        super().__init__(fname, lname, salary)
        self.salesnum=salesnum
        self.comrate=comrate

    def calpaycheck(self):
        regular_salary= super().calpaycheck()
        total_commission=self.salesnum*self.comrate
        return regular_salary+total_commission
