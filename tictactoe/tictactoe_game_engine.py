class TictactoeGameEngine:
    def __init__(self):
        self.SIZE = 3
        self.board = list('.' * self.SIZE * self.SIZE) # ['.', '.', '.', '.', '.', '.', '.', '.', '.']
        self.turn ='X'

    def show_board(self):
        print(self.board)

    def set(self, row, col):
        pass

    def set_winner(self):
        # -가로 세줄
        # |세로 세줄
        # \/대각선 두줄 (0, 4, 8)(2, 4, 6)
        for n in range(0, 9):
            
        # 비기는 조건: 다 채워졌을 때 위의 것에 해당이 안됬을 때: self.board에 '.'이 없는 상태
        return self.turn
        return 'd' #draw

    def change_tryn(self):
        # self.turn 'X'면 'O', 'O'면 'X'로 표시
        pass


if __name__ == '__main__':
    game_engine = TictactoeGameEngine()  # ...\n...\n...\n
    game_engine.show_board()
    game_engine.set(3, 2)
    game_engine.show_board()   # ['.', '.', '.', '.', '.', '.', '.', '.X, '.']
    game_engine.set(3, 1)
    game_engine.set(3, 3)
    print(game_engine.set_winner())  #'X'
    game_engine.change_tryn()
    print(game_engine.turn)  #'O'
