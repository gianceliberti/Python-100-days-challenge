from logo import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Return a card from the deck"""
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards and return a score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose, opponent has blackjack. "
    elif user_score == 0:
        return "You win with a blackjack"
    elif user_score > 21:
        return "you are over 21, you lose"
    elif computer_score > 21:
        return "Opponent is over 21, you win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for card in range(2):
        """Assing 2 random cards for each player"""
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        """This while loop is for the user"""
        user_score = calculate_score(user_cards) 
        computer_score = calculate_score(computer_cards) 
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")


        if (user_score == 0 or computer_score == 0 or user_score > 21):
            is_game_over = True
        else:
            draw_new_card = input(f"Do you want to draw another card? type 'y' or 'n': ")
            if draw_new_card == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards) 
                if user_score > 21:
                    is_game_over = True
            else:
                is_game_over = True

    while computer_score !=0 and computer_score < 17:
        """This while loop is for the computer hand"""
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is: {user_cards}, final score: {user_score}")
    print(f"Computer hand was: {computer_cards} and score: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of BlackJack? type 'y' or 'n': ") == "y":
    print(logo)
    play_game()