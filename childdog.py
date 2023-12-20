from parentrobot import robot

class dog(robot):
    
    #by default it calls robot init method

    def makenoise(self):
        print("woof woof")
    
    # def walk(self, y):              #just to check whether the parent class or the child class works first
    #     print('hey')
        
    def eat(self):
        # super().eat()
        print("i like bacon")

germanshepherd=dog('jimmy')
germanshepherd.makenoise()
germanshepherd.walk(5)
#method overriding
germanshepherd.eat()
#if we wanted to call the parent class as well;  uncomment the super method line

