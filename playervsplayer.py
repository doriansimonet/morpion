#importer le module random
import random
#initialiser dans  a le retour de l'execution de la fonction input avec comme parametre "choississez le nombre de manche"
a = input('choisissez le nombre de manche: ')
#initialiser dans  a le retour de l'execution de la fonction int avec comme parametre a
a = int(a)
#initaialiser 0 dans b
b = 0
#tant qua a est différent de b
while a!=b :
    #initialiser dans b le résultat de l'addition b+1
    b=b+1
    #afficher "debut du round" et la valeur de b
    print("debut du round :", b)  
    #afficher un vide pour sauter une ligne
    print()
    #definir la classeTicTacToe
    class TicTacToe:

            #definir la fonction __init__ avec comme parametre self
            def __init__(self):
                #initialiser une liste vide dans self.board
                self.board = []

            #definir create_board avec comme parametre self
            def create_board(self):
                #pour i de 0 à 3
                for i in range(3):
                    #initiamiser une liste vide dans row
                    row = []
                    #pour j de 0 à 3
                    for j in range(3):
                        #ajouter dans la liste row -
                        row.append('-')
                    #ajouter dans la liste self.board row
                    self.board.append(row)

            #definir la fonction get_random_first_player avec comme parametre self
            def get_random_first_player(self):
                #retourner le retour de l'execution de la fonction randint avec comme parametre 0, 1
                return random.randint(0, 1)

            #definir la fonction fix_spot avec comme parametre self, row, col et player
            def fix_spot(self, row, col, player):
                #initialiser player à la valeur de la liste self.board à la position [row][col]
                self.board[row][col] = player
            
            #definir la fonction is_player_win avec comme parametre self et player
            def is_player_win(self, player):
                #initialiser none a win
                win = None
                #initialiser dans n le retour de l'execution de la fonction avec comme parametre self.board
                n = len(self.board)

                # checking rows
                #pour i dans l'intervalle de n
                for i in range(n):
                    #initialiser True à win
                    win = True
                    #pour j dans l'intervalle n
                    for j in range(n):
                        #si la valeur de la liste self.board à la position [i][j] à player
                        if self.board[i][j] != player:
                            #initialiser False à win
                            win = False
                            #sortir de la fonction
                            break
                    #si win existe
                    if win:
                        #retourner win
                        return win

                # checking columns
                #pour i dans l'intervalle n
                for i in range(n):
                    #initialiser True à win
                    win = True
                    #pour j dans l'intervalle n
                    for j in range(n):
                        #si la valeur de la liste self.board à la position [j][i] est égale à player
                        if self.board[j][i] != player:
                            #initialiser False à win
                            win = False
                            #sortir de la fonction
                            break
                    #si win existe
                    if win:
                        #retourner win
                        return win

                # checking diagonals
                #initialiser True à win
                win = True
                #pour i dans l'intervalle n
                for i in range(n):
                    #si la valeur de la liste self.board à la position [i][i] est égale à player
                    if self.board[i][i] != player:
                        #initialiser False à win
                        win = False
                        #sortir de la fonction
                        break
                #si win existe
                if win:
                    #retourner win
                    return win
                #initialiser True à win
                win = True
                #pour i dans l'intervalle n
                for i in range(n):
                    #si la valeur de la liste self.board à la position [i][n - 1 - i] est égale à player
                    if self.board[i][n - 1 - i] != player:
                        #initialiser False à win
                        win = False
                        #sortir de la fonction
                        break
                #si win existe
                if win:
                    #retourner win
                    return win
                #retourner False
                return False


            #definir la fonction is_board_filled avec comme parametre self
            def is_board_filled(self):
                # pour row dans self.board
                for row in self.board:
                    #pour item dans row
                    for item in row:
                        #si item est égale à -
                        if item == '-':
                            #retourner False
                            return False
                #retournez True
                return True

            #definir la fonction swap_player_turn avec comme parametre self et player
            def swap_player_turn(self, player):
                #retourner "X" si player est égale à "O" sinon retourner "O"
                return 'X' if player == 'O' else 'O'

            #definir la fonction show_board avec comme parametre self
            def show_board(self):
                #pour row dans self.board
                for row in self.board:
                    #pour item dans row
                    for item in row:
                        #afficher item, " "
                        print(item, end=" ")
                    #afficher un vide pour sauter une ligne
                    print()

            #definir la fonction start avec comme parametre self
            def start(self):
                #éxécuter la fonction create_board
                self.create_board()
                #initialiser une liste vide à check
                check=[]
                #initialiser une liste vide à coord
                coord =[]
                #initialiser "X" si le retour de l'éxecution de la fonction get_random_first_player est égale à 1 sinon initialiser "O"
                player = 'X' if self.get_random_first_player() == 1 else 'O'
                #Tant que True
                while True:
                    #swapping the turn
                    #initialiser le retour de l'execution swap_player_turn avec comme parametre player dans player
                    player = self.swap_player_turn(player)
                    #afficher "Player" player "turn"
                    print(f"Player {player} turn")
                    #executer la fonction showboard
                    self.show_board()

                    # taking user input
                    #initaialiser à row et col le retour de l'execution de la fonction input avec comme parametre "enter row and column number to fix spot"
                    row, col = list(
                        map(int, input("Enter row and column numbers to fix spot: ").split()))
                    # initialiser à coord une liste avec comme valeur row et col
                    coord=[row, col]
                    #pour i dans check
                    for i in check:
                        #si coord est égale à i
                        if coord == i:
                            #initaialiser à row et col le retour de l'execution de la fonction input avec comme parametre "This place is take, please enter an other row and column numbers to fix spot:"
                            row, col = list(
                            map(int, input("This place is take, please enter an other row and column numbers to fix spot: ").split()))
                    #ajouter dans la list check coord
                    check.append(coord)
                    #afficher un vide pour sauter une ligne
                    print()

                    # fixing the spot
                    # executer la fonction fix_spot avec comme parametre row -1, col -1, et player
                    self.fix_spot(row - 1, col - 1, player)

                    # checking whether current player is won or not
                    #si le retour de l'execution de la fonction is_player_win avec comme parametre player est Vraie
                    if self.is_player_win(player):
                        #afficher ("Player", player, "wins the game!")
                        print(f"Player {player} wins the game!")
                        #sortir de la fonction
                        break

                    # checking whether the game is draw or not
                    #si  le retour de l'execution de la fonction is_board_filled avec comme parametre player est Vraie
                    if self.is_board_filled():
                        #afficher "Match Draw"
                        print("Match Draw!")
                        #sortir de la fonction
                        break
                    # si le retour de l'execution de la fonction is_player_win avec comme parametre player est vraie
                    if self.is_player_win(player):
                        #afficher "player", player, "wins the game!"
                        print(f"Player {player} wins the game!")
                        #sortir de la fonction
                        break

                # showing the final view of board
                #afficher un vide pour sauter une ligne
                print()
                #executer la fonction show_board
                self.show_board()
                #afficher un vide pour sauter une ligne
                print()
                #afficher "fin du round numéro :", b
                print("fin du round numéro :", b) 
                #afficher un vide pour sauter une ligne
                print()     

    # starting the game
    #initialiser la classe TicTacToe dans tic_tac_toe
    tic_tac_toe = TicTacToe()
    #executer la fonction start 
    tic_tac_toe.start()