#Adrian Alvarado
import random

#functions
def number_guesser():
    easy_num = (random.randint(1, 5))
    medium_num = (random.randint(1, 10))
    hard_num = (random.randint(1, 20))
    diff = input("Welcome! Choose a difficulty!(Easy,Medium,Hard)")
    if diff == "Easy" or diff == "easy":
        easy_guess = int(input("I am thinking of a number 1-5. Can you guess it? "))
        if easy_num == easy_guess:
            print("Correct! The answer was " + str(easy_num))

        else:
            print("Incorrect! The answer was " + str(easy_num))

    if diff == "Medium" or diff == "medium":
        medium_guess = int(input("I am thinking of a number 1-10. Can you guess it? "))
        if medium_num == medium_guess:
            print("Nice Job! The answer was " + str(medium_num))

        else:
            print("Incorrect! The answer was " + str(medium_num))

    if diff == "Hard" or diff == "hard":
        hard_guess = int(input("I am thinking of a number 1-20. Can you guess it? "))
        if hard_num == hard_guess:
            print("Fantasic! The answer was " + str(hard_num))

        else:
            print("Incorrect! The answer was " + str(hard_num))


#main
number_guesser()
