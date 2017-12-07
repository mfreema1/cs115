class Board(object):
    def __init__(self, width=7, height=6):
        self.__width = width
        self.__height = height
        self.__board = []
        for row in range(height):
            self.__board.append([])
            for _ in range(width):
                self.__board[row].append(' ')

    def __str__(self):
        boardstr = ""
        for row in range(self.__height):
            for col in range(self.__width):
                boardstr += "|" + self.__board[row][col]
            boardstr += "|\n"
        boardstr += "-" * (self.__width * 2 + 1) + "\n"
        for col in range(self.__width):
            boardstr += ' ' + str(col)
        boardstr += ' '
        return boardstr

    def allowsMove(self, col):
        if col not in range(self.__width):
            return False
        for row in range(self.__height):
            if self.__board[row][col] == ' ':
                return True
        return False

    def addMove(self, col, ox):
        for row in range(self.__height):
            if self.__board[row][col] != ' ':
                self.__board[row - 1][col] = ox
                return
        self.__board[self.__height - 1][col] = ox

    def delMove(self, col):
        for row in range(self.__height):
            if self.__board[row][col] != ' ':
                self.__board[row][col] = ' '
                return

    def setBoard( self, moveString ):
        nextCh = 'X' # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'

    def winsFor(self, ox):
        for row in range(self.__height):
            for col in range(self.__width):
                if self.__board[row][col] == ox: #it's a match, check all the cases
                    #horiz checks going left
                    if col >= 3:
                        if self.__board[row][col - 1] == ox and self.__board[row][col - 2] == ox and self.__board[row][col - 3] == ox:
                            return True
                    #vert checks going upward
                    if row >= 3:
                        if self.__board[row - 1][col] == ox and self.__board[row - 2][col] == ox and self.__board[row - 3][col] == ox:
                            return True
                    #left-diag checks going upward and left:
                    if col >= 3 and row >= 3:
                        if self.__board[row - 1][col - 1] == ox and self.__board[row - 2][col - 2] == ox and self.__board[row - 3][col - 3] == ox:
                            return True
                    #right-diag checks going upward and right:
                    if col <= self.__width - 4 and row >= 3:
                        if self.__board[row - 1][col + 1] == ox and self.__board[row - 2][col + 2] == ox and self.__board[row - 3][col + 3] == ox:
                            return True
        return False

    def hostGame(self):
        nextChar = 'O'
        while(not self.winsFor('X') and not self.winsFor('O')):
            if nextChar == 'X': nextChar = 'O'
            else: nextChar = 'X'
            print(self)
            turn = int(input(nextChar + "\'s choice: "))
            while(not self.allowsMove(turn)):
                turn = int(input("Invalid turn. Try again: "))
            self.addMove(turn, nextChar)
        print(self)
        if(self.winsFor('X')):
            print("\nX wins! -- Congratulations!")
        else:
            print("\nO wins! -- Congratulations!")
