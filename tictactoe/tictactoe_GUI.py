from tictactoe_game_engine import TictactoeGameEngine
import tkinter

class TictactoeGUI:
    def __init__(self):
        self.game_engine = TictactoeGameEngine()
        self.init_GUI()

    def init_GUI(self):
        self.CANVAS_SIZE = 300
        self.root = tkinter.TK()
        self.root.title('틱텍토')
        self.root.geometry(f'{self.CANVAS_SIZE}x{self.CANVAS_SIZE}') #300x300
        self.root.resizable(False, False)

    def click_handler(self, event):
        pass

    def draw_boare(self):
        pass


if __name__ == '__main__':
    ttt_GUI = TictactoeGUI()