Source Repository - 
Application review - https://youtu.be/njWQ20dnUwk
Code Styling / Styling Conventions - 
The code follows the Python PEP 8 style guide,this includes but is not limited to;

Indentation of 4 spaces (no tabs).

Maximum line length of 79 characters.

Use of snake_case for variable and function names.

Use of docstrings for documenting functions and modules.

Use of single quotes for string literals.

Use of list comprehensions where appropriate.

Overall, making it more readable and maintainable.



Features included within applicaton - 

Input validation, when the user is prompted to select two cards, the program should check if the input is valid. For example, it should check if the cards are in the user's hand and if they are different from each other. If the input is invalid, the program should prompt the user to enter valid input again.

Score tracking, the program should keep track of each player's score as they find pairs. The score is the number of pairs that the player has found so far. The program should display the current score of each player after each turn.

Option to play again, after the game is over, the program should prompt the user if they want to play again. If the user enters "y" or "Y", the program should reset the game and start again. If the user enters "n" or "N", the program should exit. If the user enters any other input, the program should display an error message and prompt the user again.

File Handling, where information from the users game is stored, this includes pairs matched and end game results.

The provided features cover the criteria of demonstrating understanding of variables and variable scope, loops and conditional control structures, and error handling.


Implementation Plan - 

Define the cards

    Tasks:
    Create a list of suits and values
    Generate a list of all possible card combinations
    Store the card combinations in a list
    Implement a function to print the list of cards
    Implement error handling to ensure that cards are valid
    
    Define the suits and  values:
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'] 

    Create a lis of cards by iterating over suits and values:
    
    cards = []
for suit in suits:
    for value in values:
        cards.append(f'{value} of {suit}')  
        

    
    
Priority: High

Duration: 1 day

Feature 2: Shuffle the cards

    Tasks:

    Import the random module
    Use the shuffle method to shuffle the list of cards
    Implement a function to print the shuffled list of cards
    Implement error handling to ensure that cards are shuffled properly
 
    Use random the 'random.shuffle()' function to shuffle the 'cards' list:
# Shuffle the cards
random.shuffle(cards)

Priority: High

Duration: 1 day

Feature 3: Deal the cards

    Tasks:

    Determine the number of players
    Divide the deck of cards into hands for each player
    Implement a function to print each player's hand
    Implement error handling to ensure that hands are dealt properly

    Specify the number of players: 
   
# Deal the cards
    num_players = 2

    Determain the number of cards per player:
    
    num_cards_per_player = int(len(cards) / num_players)
    
    Create a list of hands by slicing the 'cards' list and joining the cardds in each hand with newline characters:
   
    hands = ['\n'.join(cards[i:i+num_cards_per_player]) for i in range(0, len(cards), num_cards_per_player)]
    
    
Priority: High

Duration: 1 day

Feature 4: Check for pairs

    Tasks:

    Check each player's hand for pairs
    Implement a function to print the number of pairs in each hand
    Implement error handling to ensure that pairs are checked properly
    
    use a nested loop to check each card in each hand  for a pair:
   
# Check if each hand has at least one pair
hands_have_pair = False
for hand in hands:
    for card in cards:
        if hand.count(card) == 2:
            hands_have_pair = True
            break
    if hands_have_pair:
        break
    
    Use a while loopto repeadly shuffle and deal the cardds until hand has at least one pair:
    
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
    
Priority: Medium

Duration: 1 day

Feature 5: Play the game

   Tasks:

    Allow each player to take turns flipping over cards
    Implement a function to print the cards flipped over by each player
    Determine if a pair has been found
    Remove the pair of cards from the player's hand
    Implement error handling to ensure that the game is played properly


    Use a loop to continue playing until all cards have been matched or the players choose to stop:
    #Play the game
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

Priority: High

Duration: 2 days

Feature 6: Determine the winner

    Tasks:

    Count the number of pairs in each player's hand
    Determine the winner based on the player with the most pairs
    Implement a function to print the winner
    Implement error handling to ensure that the winner is determined properly

Priority: High

Duration: 1 day

Feature 7: Save the game results

    Tasks:

    Save the winner and number of pairs to a file
    Implement a function to read the file and display the game results
    Implement error handling to ensure that game results are saved and read properly

Priority: Low

Duration: 1 day

Deadline: 7 days

#Testing used

Test for matching cards:

Start the game and select two cards from one player's hand that match (i.e., have the same value and suit).

The game should remove those two cards from the player's hand and print a message that says "You found a pair!".

Verify that the player's hand now has two fewer cards and that the two matching cards are no longer in the hand.


Test for winner determination:

Start the game and play until all pairs have been found.

The game should print a message announcing the winner(s) and the number of pairs they found.

Verify that the message accurately reflects the winner(s) and the number of pairs they found. Also, verify that the game_results.txt file contains the same message.

