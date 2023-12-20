class robot:
    def __init__(self,name):
        self.name=name
        self.position=[0,0]
        print("my name is: ",self.name)

    def walk(self,x):
        self.position[0]=self.position[0]+x
        print("my new position is: ",self.position)