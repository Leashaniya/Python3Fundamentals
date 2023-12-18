
class robotdog:
    def __init__(self,name,breed):       #name and breed are properties
        self.name=name
        self.breed=breed

dog=robotdog('jimmy','anybreed')
print(dog.name)
print(dog.breed)

#now gonna add behaviors
#creating a class method
#we create a class method just like a function Except a method has self as the first parameter

class robot_dog:
    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    def bark(self):                         #bark is a method or behavior
        # print("woof woof")
        return "woof"
doggy=robot_dog('jimmy','anybreed')
# print(doggy.name)
# print(doggy.breed)
# doggy.bark()
print(doggy.bark())