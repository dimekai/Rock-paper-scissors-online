class Game:
    def __init__(self, id):
        self.id = id
        # Take control turns for each player 
        self.player1_went = False
        self.player2_went = False
        self.ready = False
        self.moves = [None, None]
        self.wins = [0, 0]
        self.tie = 0
    
    def get_player_move(self, player):
        '''
        Getting player moves. When player is 0
        it indicates player 1, otherwise player 2

        Parameters
        ----------
            player [0, 1]: int
                - Number of player (index of self.moves list)
        
        Return
        ------
            move [Scissors, Paper, Rock]: Move class
        '''
        return self.moves[player]

    
    def player(self, player, move):
        '''
        Indicate who player moved
        '''
        self.moves[player] = move
        if player == 0:
            self.player1_went = True
        else:
            self.player2_went = True
        
    
    def is_connected(self):
        '''Indicates if the two players are currently connected to the game'''
        return self.ready
    

    def both_went(self):
        '''Indicates if the two players already moved'''
        return self.player1_went and self.player2_went
    

    def who_won(self):
        '''
        Indicates who is won the game, checking 
        their moves against one another
        
        moves: [R]ock, [S]cissors, [P]aper
        '''
        # Getting only the first letter to compare
        # [R]ock, [S]cissors, [P]aper
        player1 = self.moves[0].upper()[0]
        player2 = self.moves[1].upper()[0]

        # [-1] Tie, [0] Player1 won, [1] Player2 won
        winner = -1
        if player1 == 'R' and player2 == 'S':
            winner = 0
        elif player1 == 'S' and player2 == 'R':
            winner = 1
        elif player1 == 'P' and player2 == 'R':
            winner = 0
        elif player1 == 'R' and player2 == 'P':
            winner = 1
        elif player1 == 'S' and player2 == 'P':
            winner = 0
        elif player1 == 'P' and player2 == 'S':
            winner = 1
        
        return winner

    
    def reset_went(self):
        '''Reset the turns to play again'''
        self.player1_went = False
        self.player2_went = False

    
