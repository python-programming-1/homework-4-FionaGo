import random

def main():
    player_move()

def player_move():

    player = str(input(
        "r' for rock, 'p' for paper, 's' for scissors and 'y' for yes and 'n' for no, 'sc' for score\n"
        )).lower()

    computer = random.choice(['r', 's', 'p'])

    player_score = 0
    computer_score = 0

    if (player == 'r' and computer == 's') or \
        (player == 's' and computer == 'p') or \
        (player == 'p' and computer == 'r'):

        player_score += 1
        computer_score = computer_score

        print('you win!\n', 'player score:', player_score, 'computer score:', computer_score)

    elif (player == 's' and computer == 'r') or \
        (player == 'r' and computer == 'p') or \
        (player == 'p' and computer == 's'):

        computer_score += 1
        player_score = player_score

        print('you lose!\n', 'player score:', player_score, 'computer score:', computer_score)

    elif player == computer:

        computer_score = computer_score
        player_score = player_score

        print('draw!\n', 'player score:', player_score, 'computer score:', computer_score)

    return player_score, computer_score

if __name__ == "__main__":
    main()


