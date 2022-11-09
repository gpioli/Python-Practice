### Project: rock, paper scissors ###

user_option = input('rock, paper, scissors => ')
computer_option = 'scissors'

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