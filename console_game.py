import connect_four

def welcome_banner():
    ''' Prints welcome in the console '''
    print("Welcome to the Connect Four Game!")
    print()
    
def ask_player_for_column_number(player):
    ''' Asks player explicitly for a column after every turn '''
    print("It's now player's %d turn" % (player))
    print('To choose a column, enter a number 1 - 7')
    while True:
        # Asks the player for a number
        user_column_choice = int(input())
        # Checks whether input is not a column number, column numbers are 1 through 7
        if user_column_choice < 1 or user_column_choice > 7:
            # If number is invalid, ask again
            continue
        else:
            # Returns the user's choice
            return user_column_choice
    
def move_is_valid():
    ''' Prints OKAY after every move, if and only if it is a valid move'''
    print()
    print('OKAY')
    print()
    
def move_is_invalid():
    ''' Prints out Illegal move when a player tries to put a chip in a full column '''
    print()
    print('ILLEGAL MOVE')
    print()
    
def connect_four_game():
    ''' Plays the connect four game '''
    # Displays a welcome to the user(s)
    welcome_banner()
    # Creates a game object
    game = connect_four.Board()
    # Overrides the method __repr__ and prints out an empty board
    print(game)
    print()
    # This loop allows the game to be played, and will stop until a game is won
    # or game ends in a draw
    while True:
        # Asks and obtains player's column of choice
        player_column_choice = ask_player_for_column_number(game.current_player)
        # If expression checks if the player's column choice is a valid choice
        if game.make_move(game.current_player, player_column_choice):
            # If move is valid, prints "OKAY" for user clarification
            move_is_valid()
            # Prints the board with the player's column choice
            print(game.get_board())
            # flag is a tuple that contains 3 elements: 
                # a tuple with three elements is returned by game.is_game_over.
                # is_game_over() returns a tuple with three elements that will help define
                # whether, 'someone won', 'game ended in a draw' or 'no winner' 
                # flag[0] = boolean value 1, flag[1] = boolean value 2, flag[2] = the winner 
            # flag[2] -> Returns 1 if player 1 wins, 2 if player 2 wins, 0 if no one wins
            flag = game.is_game_over() 
            # if both of the boolean values are True, then it means that the game is over and it is a draw, no one wins.
            if flag[0] and flag[1]:
                print("\nGame Over!")
                print("It's a draw")
                break
            # If the first boolean value is True
            elif flag[0] or flag[1]:
                print("\nGame Over!")
                print("Player %d wins!" % (flag[2]), end='')
                break
            # Control is handed to the next player
            game.whose_turn_is_it()     
        else:
            # If a move was invalid, i.e., player chose a column with full entries, then here prints out "Illegal Move"
            move_is_invalid()
    
if __name__ == '__main__':
    connect_four_game() 
