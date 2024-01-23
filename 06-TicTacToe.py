import random
import time

def show():
    for row in game_board:
        for cell in row:
            if cell == "O":
                print("\033[34m" + cell + "\033[0m", end=" ")
            elif cell == "X":
                print("\033[31m" + cell + "\033[0m", end=" ")
            else:
                print(cell, end=" ")
        print()

def get_input():
        while True:
            row = int(input("row: "))
            col = int(input("col: "))
            if row in [0, 1, 2] and col in [0, 1, 2] :
                break
            else:
                print("choose in [0,2]")
        return row, col

def check_game():
    winner = None
    if game_board[0][0] == game_board[1][1] == game_board[2][2] != "_":
        winner = game_board[0][0]
    elif game_board[0][2] == game_board[1][1] == game_board[2][0] != "_":
        winner = game_board[0][2]
    
    for i in range(3):
        if game_board[i][0] == game_board [i][1] == game_board [i][2] !="_":       
            winner = game_board[i][0]
            break    
    for j in range(3):
        if game_board[0][j] == game_board [1][j] == game_board [2][j] !="_":
            winner = game_board[0][j]
            break
    if winner is None and all("_" not in row for row in game_board):
        winner = "Nobody"
    return winner

def show_time():
    end_time = time.time()
    game_time = int(end_time - start_time)
    print ("duration was: ", game_time, "seconds.")
    
                   
    
start_time = time.time()
print ("start is : ", start_time)
game_board = [["_","_","_"],
              ["_","_","_"],
              ["_","_","_"]]

while True:
    player_numbers = int(input("Enter number of players '1' or '2': "))
    if player_numbers in [1, 2]:
        break
    else:
        print("Only enter '1' or '2'")



while True:        
    while True:
        show()
        print("player X")
        row, col = get_input()
        if game_board[row][col] == "_":
            game_board[row][col] = "X"
            
            winner = check_game()
            if winner:
                show()
                break
            break
        else:
            show()
            print()
            print("Already chosen!; Try another")
    if winner:
        if winner == "Nobody":
            print("Its a tie")
            show_time()
        else:
            print("Player ", winner, " won")
            show_time()
        break
    
    if player_numbers == 2:
        while True:
            show()
            print("player O")
            
            row, col = get_input()
            if game_board[row][col] == "_":
                game_board[row][col] = "O"
                
                winner = check_game()
                if winner:
                    show()
                    break
                break
            else:
                show()
                print()
                print("Already chosen!; Try another")
        if winner:
            if winner == "Nobody":
                print("Its a tie")
                show_time()
            else:
                print("Player ", winner, " won")
                show_time()
            break

    elif player_numbers == 1:
        while True:
            show()
            print("player O (computer)")
            empty_cells = []
            for i in range(3):
                for j in range(3):
                    if game_board[i][j] == "_":
                        empty_cells.append((i ,j))
            random_cell = random.choice(empty_cells)            
            game_board[random_cell[0]][random_cell[1]] = "O"
            winner = check_game()
            if winner:
                show()
                break
            break

        if winner:
            if winner == "Nobody":
                print("Its a tie")
                show_time()
            else:
                print("Player ", winner, " won")
                show_time()
                break        