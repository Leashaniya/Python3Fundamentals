
def greeting(name):
    print("hello",name)

#greeting function name 
#name is the paramter 
#name in local scope

#main program using local scope
input_name1=input("enter your name: ")
input_name2=input("enter your name: ")

greeting(input_name1)
greeting(input_name2) 


#if name is in global scope

def greetings():
    print("hi ",name1)

name1=input("enter your name: ")
greetings()
name2=input("enter your name: ")
name1=name2

greetings()
