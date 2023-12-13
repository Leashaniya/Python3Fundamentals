import random
computer_choice=random.choice(['rock','paper','scissors'])

user_choice=input("you want rock,paper or scissors?")
#print('computer choice was: '+computer_choice)
print('computer choice was: ',computer_choice)
if computer_choice==user_choice:
    print("TIE")
elif computer_choice=='scissors' and user_choice=='rock':
    print("you win")
elif user_choice=='paper' and computer_choice=='rock':
     print("you win")

elif user_choice=='scissors'  and computer_choice=='paper':
     print("you win")
else:
    print("you lost")
