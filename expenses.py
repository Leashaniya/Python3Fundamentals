expenses=[10.5,8,5,15,20,5,3]
sum=0

for result in expenses:
    sum=sum+result

#if we use comma to concatenate then we don't need to covert the sum to a string while printing
print("you spent",sum)
print("you spent $",sum)
#automatically we get a space after the string and before the sum
#if we don't need the space
print("you spent $",sum,sep='')
