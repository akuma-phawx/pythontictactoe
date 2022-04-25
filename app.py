row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']


playerPlaying = 1
gameOver = False


def displayTable(row1="No row1 is given", row2="No row2 is given", row3="No row3 is given"):
    print(row1)
    print(row2)
    print(row3)


def introduction():
    print('Welcome to Tic Tac Toe!\n')
    player_one = input('\t Player 1 name: ')
    player_two = input('\t Player 2 name: ')
    print(f'\n{player_one} (O) vs {player_two} (X).. Let the game begin!')


def start_game():
    while not gameOver:
        displayTable(row1, row2, row3)


def check_if_winner():
    pass


introduction()
start_game()
