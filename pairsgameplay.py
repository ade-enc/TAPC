# Play the game
scores = [0] * num_players
rounds = 1
while len(cards) > 0:
    print(f"Round {rounds}")
    for i in range(num_players):
        print(f"Player {i+1}'s turn.")
        print("Cards in your hand:")
    for card in hands[i]:
            print(card)
    card1 = input("Choose the first card you want to flip over: ")
    card2 = input("Choose the second card you want to flip over: ")
    if hands[i].count(card1) == 1 and hands[i].count(card2) == 1 and card1!= 
    card2:
            hands[i].remove(card1)
            hands[i].remove(card2)
            print("You found a pair!")
            scores[i] += 1
    else:
            print("Those cards don't match or you don't have them in your hand.")
    if len(cards) == 0:
            break
    rounds += 1           
    #Must define features
    #