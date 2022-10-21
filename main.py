
def board(spaces):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(spaces[0], spaces[1], spaces[2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(spaces[3], spaces[4], spaces[5]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(spaces[6], spaces[7], spaces[8]))
    print("\t     |     |")
    print("\n")

def move(players_choices, current_player):
        player_move = int(input(f"{current_player} Which space: "))
        while player_move in players_choices["X"] or player_move in players_choices["O"]:
            print("space is already taken, try again")
            player_move = int(input(f"{current_player} Which space: "))

        else:
            return player_move

def checkwin(players_choices, current_player):
    winning = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
    for x in winning:
        if all(y in players_choices[current_player] for y in x):
            return True
    return False

def draw(players_choices):
    if len(players_choices["X"]) + len(players_choices["O"]) == 9:
        return True
    return False       

def game():
    spaces = [" " for x in range(9)]
    board(spaces)
    players_choices = {"X":[], "O":[]}
    player_1 = "X"
    player_2 = "O"
    current_player = player_1


    while True:
        player_move = move(players_choices, current_player)
        spaces[player_move-1] = current_player
        players_choices[current_player].append(player_move)
        if checkwin(players_choices, current_player):
            print(f"{current_player} has won")
            board(spaces)
            break
        if draw(players_choices):
            print("Game is a draw")
            board(spaces)
            break
        board(spaces)
        if current_player == player_1:
            current_player = player_2
        elif current_player == player_2:
            current_player = player_1

    play_again = input("play again? yes or no ").lower()
    if play_again == "yes":
        game()
    else:
        print("thank you for playing")


game()




