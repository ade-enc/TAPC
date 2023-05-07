
# Define the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards = []
for suit in suits:
    for value in values:
        cards.append(f'{value} of {suit}')

# shuffle card deck
random.shuffle(cards)
#Use code below due to not getting pairs in game
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
