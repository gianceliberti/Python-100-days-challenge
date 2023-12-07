from art import logo,vs
from data import data
import random

def get_data():
    """Selecciona dos elementos aleatorios de la lista data"""
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_data()
    account_b = get_data()
    
    while game_should_continue:
        account_a = account_b
        account_b = get_data()

        while account_a == account_b:
            account_b = get_data()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Againts B: {format_data(account_b)}")
        decision = input(f"Who has more followers? Type 'A' or 'B': ")
        followers_a = account_a["follower_count"]
        followers_b = account_b["follower_count"]
        if (followers_a > followers_b and decision.upper() == 'A') or (followers_b > followers_a and decision.upper() == 'B'):
            score += 1
            print(f"You are right, current score {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            break

game()

