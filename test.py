# create a score report
# if a user types a then +1; if a user types b then 0
# a user stop typing, then a report generated

def main():
    #summing()
    #mySum()
    typing_game()

def mySum():
    mySum = 0
    for num in range(1,3):
        mySum +=num
    print(mySum)

def summing():

    for i in range(1,11):

        score = 0
        score += i

        return score

        print(score)


def typing_game():
    user_input = str(input("type a then plus one, type b plus a zero:"))
    score_report = 0

    for score in range(1,3):
        if user_input == 'a':
            score_report += score

        elif user_input == 'b':
            score_report += 0

    print(score_report)



if __name__ == '__main__':
    main()