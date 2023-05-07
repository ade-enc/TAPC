 # Write game results to file
with open('game_results.txt', 'a') as f:
    f.write(f"Player {winner+1} wins!\n")  