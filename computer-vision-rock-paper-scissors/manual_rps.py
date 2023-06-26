## import the relevant tools for the game
import random



def get_computer_choice(word_list):
    return random.choice(word_list)

def get_user_choice():
    return input("Play it is your turn: ")

## Define a function and within the function create the conditions to determine the winner of the game

def get_winner(computer, user):
    if computer == user:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "You wins!"
    else:
        return "Computer win!"

def play_game():
    word_list = ['rock', 'paper', 'scissors']
    computer = get_computer_choice(word_list)
    user = get_user_choice()
    print("You selected:", user)
    print("The computer selected:", computer)
    result = get_winner(computer, user)
    print(result)

play_game()
