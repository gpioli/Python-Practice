### Project: rock, paper scissors ###

# Here we import random
import random

options = ("rock", "papper", "scissors")

print("Welcome to rock, papper, scissors game!")
user_option = input('Please, write your choice: rock, paper, scissors => ').lower()

if not user_option in options:
    print("You entered an invalid option")


computer_option = random.choice(options)

print("User opton =>", user_option)
print("Computer option=>", computer_option)

if user_option == computer_option:
    print("It's a tie!")
elif user_option == 'rock':
    if computer_option == 'scissors':
        print("Rock wins over scissors!")
        print("You win!")
    else:
        print("Papper wins over rock!")
        print("Computer wins!")
elif user_option == 'papper':
    if computer_option == 'rock':
        print('Papper wins over rock')
        print('You win!')
    else:
        print('Scissors win over papper!')
        print('Computer wins!')
elif user_option == 'scissors':
    print('Scissors wins over papper!')
    print('You win!')