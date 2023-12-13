import random

roll=random.randint(1,6)
guess=int(input("guess the dice roll: "))

if roll==guess:
    print("your guess is correct and it is "+str(roll))
else:
    print("your guess is wrong and the roll number is "+str(roll))
