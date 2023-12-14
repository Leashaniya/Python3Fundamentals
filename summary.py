import random
'''run python and explore data types'''
#-------------------------------------------
#introducing data types
# print("hello world")     #string
# length=10               #integer
# width=100.5             #float
# area = length* width
# print(area)



# #tax calculator
# amount =200
# tax=0.07
# total=amount + amount*tax
# print(total)



# #data type conversion functions
# '''float to int'''
# amount=int(10.6)
# print(amount)
# '''int to a float'''
# money=float(50)
# print(money)



# #string
# name="Sarah's store"
# print(name)
# hello= "hello"
# name1= "sarah"
# greeting=hello+name1          #when putting + we don't get space inbetween
# print(greeting)  
# greeting1=hello+' '+name1     #concatenating a space
# print(greeting1) 
# print(hello,name1)            #when putting , we get space inbetween



# #input function
# name2=input("what's your name\n")     # \n \t 
# greeting2=hello+" "+name2
# print(greeting2)



# #age calculator
# old=int(input("enter your age\n"))
# decade = old//10
# year= old%10
# print("you are",decade,"decades and",year,"years old")                   #this is the good way o write using ,
# print("you are "+str(decade)+" decades and "+str(year)+" years old")     #when using + you have to change the type of the variable to string 


# '''conditional and imports'''
# #---------------------------------
# #if,elif,else
# #eg 01:
# temp=int(input("enter the temperature\n"))
# if temp>80:
#     print("it's hot")
# elif temp<60:
#     print("stay inside")
# else:
#     print("go outside")
# print("have a nice day")
# #eg 02:
# temperature=int(input("enter the temperature\n"))
# forecast=input("enter the forecast\n")
# if temperature<80 and forecast !='rainy':    #not forecast== 'rainy'    can use or ,and--> logical operators 
#     print('go outside')
# else:
#     print("stay inside")
# #eg 03:
# raining=True
# if raining:
#     print("stay inside")
# else:
#     print("go outside")



# #importing python modules
# roll=random.randint(1,6)
# print(roll)
# choose=random.choice(['rock','paper','scissors'])
# print(choose)



'''list and loops'''
#-----------------------
emptylist=[]
emptylist.append("hi")
emptylist.append("hello") 
emptylist.append("how are you") 
emptylist.append("how you doing")  #append is a method ; object is a list we created 
print(emptylist[0])
print(emptylist)
emptylist.remove("hi")             #removing by giving the content in the list
del emptylist[0]                   #removing by giving the index of the list
print(emptylist)                   #remove is a method

if 1 in [1,2,3,4]:
    print(True)                    #checking the item is in the list

for result in emptylist:
    print(result)                #printing the item in the list in each line

#sum of expenses 
expense=[10,140,85,60,12]
tot=0
for x in expense:
    tot=tot+x
print(tot)
#ways of printing the output
print("you spent",tot)
print("you spent $",tot)         #space between $ and the amount
print("you spent $",tot,sep='')  #no space between $ and the amount

#sum function
total=sum(expense)               #sum is a function
print(total)

#loops with range 
for i in range(1,7,2):
    print(i)


#expenses calculator
totals=0
expenses=[]
num_expenses=int(input("enter the number of expenses: "))
for i in range(num_expenses):
    expenses.append(float(input("enter the amount: ")))

totals=sum(expenses)

print("the total expenses is: ",totals)


