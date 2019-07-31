import random

def main():
    player_move()

def player_move():

    player = str(input(
        "r' for rock, 'p' for paper, 's' for scissors and 'y' for yes and 'n' for no, 'sc' for score\n"
        )).lower()

    computer = random.choice(['r', 's', 'p'])

    if (player == 'r' and computer == 's') or \
        (player == 's' and computer == 'p') or \
        (player == 'p' and computer == 'r'):

         print('you win!')

    elif (player == 's' and computer == 'r') or \
        (player == 'r' and computer == 'p') or \
        (player == 'p' and computer == 's'):

         print('you lose!')

    elif player == computer:
            print('draw!')

if __name__ == "__main__":
    main()


