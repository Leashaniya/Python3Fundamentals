#In this program return is used and code is organized into logical units

def addition(a,b):
    # print("total is: ",a+b)
    return a+b

#main
def main():
    num1=int(input("enter 1st number: "))
    num2=int(input("enter 2nd number: "))

    result=addition(num1,num2)
    print(result)

main()
