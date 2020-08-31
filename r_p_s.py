import random

def play():
    user = input('Choose: Rock (R), Paper (P) or Scissors (S): ')
    computer = random.choice(['R', 'P', 'S'])

    user = user.upper()

    if user == 'ROCK':
        user = 'R'
    elif user == 'PAPER':
        user = 'P'
    elif user == "SCISSORS":
        user = 'S'

    if user == 'R' or user == 'P' or user == 'S':

        if user == 'R' and computer == 'S':
            print('Computer has chosen Scissors and you have chosen Rock.')
            print('You win!')
        elif user == 'R' and computer == 'P':
            print('The computer has chosen Paper and you have chosen Rock.')
            print('You lose!')
        elif user == 'P' and computer == 'S':
            print('Computer has chosen Scissors and you have chosen Paper.')
            print('You lose!')
        elif user == 'P' and computer == 'R':
            print('Computer has chosen Rock and you have chosen Paper.')
            print('You win!')
        elif user == 'S' and computer == 'P':
            print('Computer has chosen Paper and you have chosen Scissors.')
            print('You win!')
        elif user == 'S' and computer == 'R':
            print('Computer has chosen Rock and you have chosen Scissors')
            print('You lose!')
        elif user == 'S' and computer == 'S':
            print('You and the computer have chosen Scissors!')
            print('It is a tie!')
        elif user == 'R' and computer == 'R':
            print('You and the computer have chosen Rock.')
            print('It is a tie')
        elif user == 'P' and computer == 'P':
            print('You and the computer have chosen Paper.')
            print('It is a tie!')

    else:
        print('You have entered an incorrect value.')