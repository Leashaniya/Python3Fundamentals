#two users who roll a pair of dice to see who wins
import random

def roll():
    roll=random.randint(1,6)+ random.randint(1,6)      #or can type like this -->   random.randint(2,12)
    return roll

player1=input("enter 1st player's name: \n")
player2=input("enter 2nd player's name: \n")

roll1=roll()
roll2=roll()

print(player1,"rolled",roll1)
print(player2,"rolled",roll2)

if(roll1>roll2):
    print(player1,"wins")
elif(roll2>roll1):
    print(player2,"wins")
else:
    print("draw match")