import random 

def roll():
    roll = random.randint(1,6)
    return roll 

while True:
    players = input("Enter the number of players: ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid, try again")

max_score = 50 
players_scores = [0 for i in range(players)]

while max(players_scores) < max_score:

    for players_index in range(players):
        print(f"\n Player {players_index + 1} has started\n")
        print(f"Your total score is {players_scores[players_index]}")
        current_scores = 0

        while True:
            ask_roll = input("Do you want to roll the dice? (y) ").lower()

            if ask_roll != "y":
                break 
            else:
                value = roll()

            if value == 1:
                print("You rolled a 1, Turn Done!")
                current_scores = 0
                break
            else:
                current_scores += value
                print(f"you rolled a: {value}")
            print(f"your score is {current_scores}")
        
        players_scores[players_index] += current_scores
        print(f"Your total score is  {players_scores[players_index]}")

max_score = max(players_scores)
winning_user = players_scores.index(max_score)
print(f"Player number {winning_user + 1} is the winner with a score of {max_score}")




        



