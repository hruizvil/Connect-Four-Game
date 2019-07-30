class Board:
    def __init__(self):
        ''' This is the constructor method. It is used to initialize an object for the class '''
        self.board = [['1', '2', '3', '4', '5', '6', '7'], 
                      ['.', '.', '.', '.', '.', '.', '.'], 
                      ['.', '.', '.', '.', '.', '.', '.'], 
                      ['.', '.', '.', '.', '.', '.', '.'], 
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.']
                    ]
        self.current_player = 1
        self.rows = 6
        self.columns = 7
        self.red_chip = 'R'
        self.yellow_chip = 'Y'
        
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        '''This method is used for overwriting repr, so that it prints out the
           board when called in console_game.py '''
        board = []
        # This loop is used to loop through the list of lists, so that we can 
        # print out the board
        for row in self.board:
            # Separates elements in each row, and appends each element with 
            # a separation of 2 spaces in the board list
            board.append('  '.join(row))
        # Returns the modified board list
        return '\n'.join(board)
    
    def get_board(self):
        '''This is a getter method. Returns the board from the __repr__ method'''
        return self.__str__()

    def whose_turn_is_it(self):
        ''' This is a getter method. Specifies which player plays next '''
        if self.current_player == 1: 
            self.current_player = 2
        else:
            self.current_player = 1
        print()
            
    def make_move(self, current_player, col):
        ''' This is a setter method. 
            Use it to make a move in the game.
        '''
        # This loop is used to identify whether the player's cell choice has a chip or not
        while True:
            # If player's (either player 1 or 2) input equals an empty cell
            if self.board[self.rows][col-1] == '.':
                # If the player is player 1 then put a red chip in the cell
                if self.current_player == 1:
                    self.board[self.rows][col-1] = 'R'
                # If the player is player 2 then put a red chip in the cell
                elif self.current_player == 2:
                    self.board[self.rows][col-1] = 'Y'
                # Resets row to 6 so that if player chooses an empty column,
                # then chip is allocated in the bottom
                self.rows = 6
                # Returns True if move is Valid
                return True
            # Checks if a cell contains a yellow or red chip
            elif self.board[self.rows][col-1] == 'R' or self.board[self.rows][col-1] == 'Y':
                # If cell is out of bounds, in this case the title which contains the names 1 2 3 4 5 6 7
                if self.rows == 1:
                    # Resets the rows to default cell
                    self.rows = 6
                    # Returns false if move was out of bounds
                    return False
                else:
                    self.rows -= 1
                    
    def is_game_over(self):
        ''' '''
        # check if there is a draw
        counter = 0  # this counter keeps track of how many cells that we have checked through.
        # To check if there is any unfilled cell within our board, we use a nested loop to loop through each cell of self.board
        for row in self.board:
            for col in row:
                if col != '.':
                    counter += 1
        if counter == 49:  #  since we also put the name of each column in the self.board, there are 49 elements within our board in total.
            # the first element of the returned tuple indicates whether the game is over.
            # the second element of the returned tuple indicates whether the game has reached a draw.
            # the third element of the returned tuple indicates the winner of this game.            
            return (True, True, 0)  # this result shows that the game is over, it is a draw, no one wins.
        
        # These variables specify the limits of the winning sequence
        maximum_index_vertically = self.rows - 2  # 6 - 2
        maximum_index_horizontally = 3 
        
        # check the game vertically for a win
        for x in range(self.rows):
            for y in range(maximum_index_vertically):
                if self.board[x+1][y] == self.red_chip and self.board[x+1][y+1] == self.red_chip and self.board[x+1][y+2] == self.red_chip and self.board[x+1][y+3] == self.red_chip:
                    return (True, False, 1)  # player 1 or red_chip wins
                elif self.board[x+1][y] == self.yellow_chip and self.board[x+1][y+1] == self.yellow_chip and self.board[x+1][y+2] == self.yellow_chip and self.board[x+1][y+3] == self.yellow_chip: 
                    return (True, False, 2)  # player 2 or yellow_chip wins
        
        # check the game horizontally for a win       
        for x in range(0, maximum_index_horizontally):
            for y in range(self.columns):
                if self.board[x+1][y] == 'R' and self.board[x+2][y] == 'R' and self.board[x+3][y] == 'R' and self.board[x+4][y] == 'R':
                    return (True, False, 1)  # player 1 or red_chip wins
                elif self.board[x+1][y] == 'Y' and self.board[x+2][y] == 'Y' and self.board[x+3][y] == 'Y' and self.board[x+4][y] == 'Y':
                    return (True, False, 2)  # player 2 or yellow_chip wins
        
        # check the game diagonally for a win starting from top left corner
        for x in range(maximum_index_horizontally):
            for y in range(maximum_index_vertically):
                if self.board[x+1][y] == 'R' and self.board[x+2][y+1] == 'R' and self.board[x+3][y+2] == 'R' and self.board[x+4][y+3] == 'R':
                    return (True, False, 1)  # player 1 or red_chip wins
                elif self.board[x+1][y] == 'Y' and self.board[x+2][y+1] == 'Y' and self.board[x+3][y+2] == 'Y' and self.board[x+4][y+3] == 'Y':
                    return (True, False, 2)  # player 2 or yellow_chip wins
        
        # check the game diagonally for a win starting from top right corner       
        for x in range(maximum_index_horizontally):
            for y in range(maximum_index_vertically):
                if self.board[x+1][6-y] == 'R' and self.board[x+2][5-y] == 'R' and self.board[x+3][4-y] == 'R' and self.board[x+4][3-y] == 'R':
                    return (True, False, 1)  # player 1 or red_chip wins
                elif self.board[x+1][6-y] == 'Y' and self.board[x+2][5-y] == 'Y' and self.board[x+3][4-y] == 'Y' and self.board[x+4][3-y] == 'Y':
                    return (True, False, 2)  # player 2 or yellow_chip wins

        return (False, False, None)  # game is not over
