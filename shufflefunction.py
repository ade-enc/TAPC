import random
# Define the cards
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
cards = []
for suit in suits:
    for value in values:
        cards.append(f'{value} of {suit}')

# shuffle card deck
random.shuffle(cards)
