import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False



    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()
        check=[]
        coord =[]
        #player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            player = "X"
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            coord=[row, col]
            for i in check:
                if coord == i:
                    row, col = list(
                    map(int, input("This place is take, please enter an other row and column numbers to fix spot: ").split()))
            check.append(coord)
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            #swapping the turn
            player = self.swap_player_turn(player)

            print( "It's bot turn")
            turnBot = 1
            while turnBot == 1:

                rowBot = random.randint(1,3)
                colBot = random.randint(1,3)
                coordBot = [rowBot, colBot]
                playBot = self.board[rowBot-1][colBot-1]
                if playBot == "-":
                    self.board[rowBot-1][colBot-1] = player
                    check.append(coordBot)
                    print(check)
                    turnBot = 0
                else:
                    print("test")
                    
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break
                
        # showing the final view of board
        print()
        self.show_board()
        

# starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()
