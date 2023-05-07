
#doesn't work without defining cards
# Deal the cards
num_players = 2
num_cards_per_player = int(len(cards) / num_players)
hands = [[] for _ in range(num_players)]
for i in range(num_cards_per_player):
    for j in range(num_players):
     hands[j].append(cards.pop())
