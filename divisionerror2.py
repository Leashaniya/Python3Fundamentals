#raising a custom exception
def remainder_divisions(c,d):
    if d==0:
        raise Exception("divisor cannot be zero") 
    result=c//d
    remainder=c%d
    print(c,'/',d,'is',result,'and the remainder is',remainder)

remainder_divisions(5,0)