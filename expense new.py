tot=0
expense=[]
num_expenses=int(input("enter the number of expenses you wanted to enter "))
for i in range (num_expenses):
    i=float(input("enter the expense: "))
    expense.append(i)
    #expense.append(float(input("enter the expense: ")))

tot=sum(expense)
print("you spent $",tot,sep='')

