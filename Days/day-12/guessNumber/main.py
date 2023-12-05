from logo import logo
import random

EASY_LIFES = 10
HARD_LIFES = 5

#Function to set difficulty.
def set_difficult():
    level = input("Chose a difficulty, typw 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LIFES
    else:
        return HARD_LIFES

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """Check the user guess againsts the answer, and returns the number of lifes."""
    if guess > answer:
        print("It's to high.")
        return turns -1
    elif guess < answer:
        print("It's too low.")
        return turns -1
    else:
        print(f"That is correct the answer was: {answer}.")


def game():
    print(logo)
    #Choose a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    test = print(f"Pssst, the correct answer is {answer}")
    print(test)

    turns = set_difficult()

    #Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a guess: "))
        #Track the number of turns and reduce by 1 if its wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You don't have any attempts left, you lose.")
            return #exit the function
        elif guess != answer:
            print("Guess again.")

game()



