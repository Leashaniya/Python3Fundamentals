class dog(robot):
    
    #by default it calls robot init method

    def makenoise(self):
        print("woof woof")

germanshepherd=robot('jimmy')
germanshepherd.makenoise()
germanshepherd.walk(5)
