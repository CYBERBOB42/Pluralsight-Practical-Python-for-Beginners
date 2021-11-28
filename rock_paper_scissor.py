import random

computer_choice = random.choice(['scissors', 'rock', 'paper'])

#computer_choice="scissors"

user_choice = input("Do you want - rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print('TIE, computer had ' + str(computer_choice))

elif user_choice =='rock' and computer_choice == 'scissors':
    print('WIN, computer had ' + str(computer_choice))
elif user_choice == 'paper' and computer_choice == 'rock':
    print('WIN, computer had ' + str(computer_choice))
elif user_choice == 'scissors' and computer_choice == 'paper':
    print('WIN, computer had ' + str(computer_choice))
else:
    print('You lose :( Computer wins :D')
    print('Computer had ' + str(computer_choice))