def remainder(a,b):
    result=a//b
    remainder=a%b
    print(a,'/',b,'is',result,'and the remainder is',remainder)

remainder(10,3)

#raising an exception
def remainder_division(c,d):
    if d==0:
        raise ZeroDivisionError   
    result=c//d
    remainder=c%d
    print(c,'/',d,'is',result,'and the remainder is',remainder)

remainder_division(8,0)


