from console import Console
from board import Board, BOMB


FLAG_ACTION = 'f'


class GameManager():
    def __init__(self, board: Board):
        self._board = board
        self._console = Console(board)

    def run(self):
        while not (self._board.bomb_exposed or self._board.all_exposed):
            self._console.show_board()
            self._console.print_status()

            action, row, column = self._console.move_input()
            if action.lower() == 'f':
                self._board.set_flag(row, column)
            else:
                self._board.expose(row, column)


        self._console.print_end(self._board.bomb_exposed)
