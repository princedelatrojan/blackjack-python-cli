import random
from art import logo  # assuming this exists and is correct

# Global card values
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(card_list):
    """Takes a list of cards and returns the score."""
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0  # Blackjack
    if 11 in card_list and sum(card_list) > 21:
        card_list[card_list.index(11)] = 1
    return sum(card_list)


def compare(user_score, computer_score):
    """Compares user and computer scores and returns the result."""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while calculate_score(computer_cards) < 17:
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Main game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    play_game()
