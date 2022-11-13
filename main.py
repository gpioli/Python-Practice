### Project: rock, paper scissors ###

# Here we import random
import random

options = ("rock", "papper", "scissors")

rounds = 1
computer_wins = 0
user_wins = 0

print("*" * 40)
print("Welcome to rock, papper, scissors game!")
print("*" * 40)
print("")

while True:

    print("*" * 10)
    print("Round: ", rounds)
    print("*" * 10)
    print("User wins: ", user_wins)
    print("Computer wins: ", computer_wins)


    user_option = input('Please, write your choice: rock, paper, scissors => ').lower()

    if not user_option in options:
        print("You entered an invalid option")
        continue

    computer_option = random.choice(options)

    print("User opton =>", user_option)
    print("Computer option=>", computer_option)

    if user_option == computer_option:
        print("It's a tie!")
    elif user_option == 'rock':
        if computer_option == 'scissors':
            print("Rock wins over scissors!")
            print("You win!")
            user_wins += 1
        else:
            print("Papper wins over rock!")
            print("Computer wins!")
            computer_wins += 1
    elif user_option == 'papper':
        if computer_option == 'rock':
            print('Papper wins over rock')
            print('You win!')
            user_wins += 1
        else:
            print('Scissors win over papper!')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'scissors':
        print('Scissors wins over papper!')
        print('You win!')
        user_wins += 1

    if computer_wins == 2:
        print("Computer wins the match!")
        break
    elif user_wins == 2:
        print("User wins the match! Congratulations!")
        break

    rounds += 1