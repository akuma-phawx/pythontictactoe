table = ['0', '1', '2', '3', '4', '5', '6', '7', '8']

available_cells = list(range(0, 9))
winning_cells = ([0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6])

players = {'1': {'name': '', 'symbol': 'X'}, '2': {'name': '', 'symbol': 'O'}}

playerPlaying = 1
gameOver = False


def print_tic_tac_toe():
    print(f"\n")
    print(f"\t     |     |")
    print(f"\t  {table[0]}  |  {table[1]}  |  {table[2]} ")
    print(f'\t_____|_____|_____')

    print(f"\t     |     |")
    print(f"\t  {table[3]}  |  {table[4]}  |  {table[5]}")
    print(f'\t_____|_____|_____')

    print(f"\t     |     |")
    print(f"\t  {table[6]}  |  {table[7]}  |  {table[8]}")
    print(f"\t     |     |")
    print("\n")


def introduction():
    print('Welcome to Tic Tac Toe!\n')
    players['1']['name'] = input('\t Player 1 name: ')
    players['2']['name'] = input('\t Player 2 name: ')
    print(
        f"\nPlayer One: {players['1']['name']} with (X) vs Player Two: {players['2']['name']} with (O).. Let the game begin!\n")


def start_game():
    introduction()
    print_tic_tac_toe()

    while not gameOver:
        cell = int(
            input(f"\n{players[str(playerPlaying)]['name']} pick a cell: "))
        while cell not in available_cells:
            cell = int(input(
                f"Cell {cell} is not available. Player {players[str(playerPlaying)]['name']} pick a cell: "))

        available_cells.remove(cell)
        table[cell] = players[str(playerPlaying)]['symbol']
        print_tic_tac_toe()
        check_if_winner()
        change_player()


def check_if_winner():
    pass


def change_player():
    global playerPlaying
    if playerPlaying == 1:
        playerPlaying = 2
    else:
        playerPlaying = 1


start_game()
