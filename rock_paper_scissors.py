import random

def main():

    game_result = human_move()
    score_counter(game_result[0], game_result[1])

    #human_move()
    #human_input()

def human_move():

    human_won = False
    computer_won = False

    human_choice = str(input(
        "Welcome! Please input r' for rock, 'p' for paper, 's' for scissors!\n"
        )).lower()

    computer_choice = random.choice(['r', 's', 'p'])

    if (human_choice == 'r' and computer_choice == 's') or \
        (human_choice == 's' and computer_choice == 'p') or \
        (human_choice == 'p' and computer_choice == 'r'):

        human_won == True and computer_won == False
        print('you win!\n')

        #print('you win!\n', 'player score:', player_score, 'computer score:', computer_score)

    elif (human_choice == 's' and computer_choice == 'r') or \
        (human_choice == 'r' and computer_choice == 'p') or \
        (human_choice == 'p' and computer_choice == 's'):

        human_won == False and computer_won == True
        print('you lose!\n')

        #print('you lose!\n', 'player score:', player_score, 'computer score:', computer_score)


    elif (human_choice == 's' and computer_choice == 's') or \
        (human_choice == 'r' and computer_choice == 'r') or \
        (human_choice == 'p' and computer_choice == 'p'):

        human_won == False and computer_won == False
        print('draw!\n')

    game_result = [human_won, computer_won]

    return game_result

def human_input():

    human_interaction = str(input(
        "Press 'y' to continue play and 'n' to discontinue, 'sc' for checking the score\n"
    )).lower()

    if human_interaction == 'y':
        print("Glad you are back!")
        human_move()
        human_input()

    elif human_interaction == 'sc':
        print("--- Score Report ---")
        score_counter(human_move())

    elif human_interaction == 'n':
        print("Thank you! See you the next time!")
        exit


def score_counter(player_a_won, player_b_won):
    score_a = 0
    score_b = 0

    if player_a_won is True and player_b_won is False:
        score_a += 1
        print("Your score is: ", score_a, "; Computer Score is:", score_b)

    elif player_a_won is False and player_b_won is True:
        score_b += 1
        print("Your score is: ", score_a, "; Computer Score is:", score_b)

    elif player_a_won is False and player_b_won is False:
        print("Your score is: ", score_a, "; Computer Score is:", score_b)

    return score_a, score_b


if __name__ == "__main__":
    main()


