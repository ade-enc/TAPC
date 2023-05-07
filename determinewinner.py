# Determine the winner
min_score = min(scores)
if scores.count(min_score) == 1:
    winner = scores.index(min_score) + 1
    print(f"Player {winner} wins with {min_score} pairs!")
    else:
    winners = [i+1 for i, score in enumerate(scores) if score == min_score]
    print(f"It's a tie between players {', '.join(map(str, winners))} with {min_score} pairs!")
    #be sure to define scores
    