# Project I: rock, paper scissors v2.0 ###

# Here we import random
import random


def choose_options():
    options = ("rock", "paper", "scissors")
    user_option = input('Please, write your choice: rock, paper, scissors => ').lower()
    computer_option = random.choice(options)

    if not user_option in options:
        print("You entered an invalid option")
        # continue
        return None

    print("User option =>", user_option)
    print("Computer option=>", computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
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
    elif user_option == 'paper':
        if computer_option == 'rock':
            print('Papper wins over rock')
            print('You win!')
            user_wins += 1
        else:
            print('Scissors win over paper!')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'scissors':
        print('Scissors wins over paper!')
        print('You win!')
        user_wins += 1
    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print("Computer wins the match!")
        return True
    elif user_wins == 2:
        print("User wins the match! Congratulations!")
        return True


print("*" * 40)
print("Welcome to rock, paper, scissors game!")
print("*" * 40)
print("")


def run_game():
    rounds = 1
    computer_wins = 0
    user_wins = 0
    winner = False
    while not winner:

        print("*" * 10)
        print("Round: ", rounds)
        print("*" * 10)
        print("User wins: ", user_wins)
        print("Computer wins: ", computer_wins)
        rounds += 1

        user_option, computer_option = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
        winner = check_winner(user_wins, computer_wins)


run_game()
