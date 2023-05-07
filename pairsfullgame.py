import random

# Define the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards = []
for suit in suits:
    for value in values:
        cards.append(f'{value} of {suit}')

# Shuffle the cards
random.shuffle(cards)

# Deal the cards
num_players = 2
num_cards_per_player = int(len(cards) / num_players)
hands = ['\n'.join(cards[i:i+num_cards_per_player]) for i in range(0, len(cards), num_cards_per_player)]
# Check if each hand has at least one pair
hands_have_pair = False
for hand in hands:
    for card in cards:
        if hand.count(card) == 2:
            hands_have_pair = True
            break
    if hands_have_pair:
        break

# If neither hand has a pair, reshuffle the cards
while not hands_have_pair:
    random.shuffle(cards)
    hands = ['\n'.join(cards[i:i+num_cards_per_player]) for i in range(0, len(cards), num_cards_per_player)]
    for hand in hands:
        for card in cards:
            if hand.count(card) == 2:
                hands_have_pair = True
                break
        if hands_have_pair:
            break


input("Let's play! Press Enter to start.\n")

# Play the game
while len(cards) > 0:
    for i in range(num_players):
        print(f"Player {i+1}'s turn.")
        print("Cards in your hand:\n" + hands[i])
        card1 = input("Choose the first card you want to flip over: ")
        card2 = input("Choose the second card you want to flip over: ")
        if card1 in hands[i] and card2 in hands[i] and card1 != card2:
            hands[i] = hands[i].replace(card1, '').replace(card2, '')
            print(f"You found a pair! {card1} and {card2} have been removed from your hand.")
        else:
            print("Those cards don't match or you don't have them in your hand.")
        if len(cards) == 0:
            break
    play_again = input("Do you want to continue playing? (y/n): ")
    if play_again.lower() == 'n':
        print("Thanks for playing!")
        exit()

# Determine the winner
score_dict = {i: num_cards_per_player - hands[i].count('\n') for i in range(num_players)}
min_score = min(score_dict.values())
winners = [i+1 for i, score in score_dict.items() if score == min_score]

# Print the winner(s)
if len(winners) == 1:
    print(f"Player {winners[0]} wins with {min_score} pairs!")
    with open('game_results.txt', 'a') as f:
     f.write(f"Player {winners[0]} wins with {min_score} pairs!\n")




