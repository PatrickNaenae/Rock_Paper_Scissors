import random

def play_game():
    choices = ['R', 'P', 'S']
    user = input("Player 1: Pick an option - 'R' for rock, 'P' for paper and 'S' for scissors: ").upper()
    while user not in choices:
        print("Please enter a valid option")
        user = input("Player 1: Pick an option - 'R' for rock, 'P' for paper and 'S' for scissors: ").upper()
    if user == 'R':
        user_choice_name = 'rock'
    elif user == 'P':
        user_choice_name = 'paper'
    elif user == 'S':
        user_choice_name = 'scissors'
    computer = random.choice(choices)
    if computer == 'R':
        computer_choice_name = 'rock'
    elif computer == 'P':
        computer_choice_name = 'paper'
    elif computer == 'S':
        computer_choice_name = 'scissors'
    print(f"Player's choice was ({user_choice_name}) : Computer's Choice was ({computer_choice_name})")

    if user == computer:
        return play_game()

    if check_winner(user, computer):
        return "You won"
 
    return 'You lost'

def check_winner(player, cpu):
    if (player == 'R'and cpu == 'S') or (player == 'P' and cpu == 'R') or (player == 'S' and cpu == 'P'):
        return True

print(play_game())


