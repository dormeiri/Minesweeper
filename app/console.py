from board import Board, FLAG, BOMB
import os


SEPERATOR = ' '
CELL_DISPLAY_MAP = {
    FLAG: 'F',
    None: '-',
    BOMB: '*'
}


class InvalidInputException(Exception):
    pass


class Console:
    def __init__(self, board: Board):
        self.board = board

    def print_end(self, game_over):
        print('Game over' if game_over else 'You won!')

    def show_board(self):
        print('\\', end="\t")
        for i in range(self.board.size):
            print(i, end=SEPERATOR)

        print()

        for i in range(self.board.size):
            row = self.board.exposed[i]
            row_display = map(Console._convert_value_to_display, row)

            print(i, end='\t')
            print(SEPERATOR.join(row_display), end='\n')

    def move_input(self):
        try:
            action = input('Action (f for flag, anything else for reveral): ')
            row = self._index_input('Row')
            column = self._index_input('Column')

            return action, row, column
        except InvalidInputException:
            print('Invalid input, insert again...')

            return self.move_input()

    def _index_input(self, name):
        value = input(f'{name}: ')
        value = self._ensure_index_input(value)

        return value

    def _ensure_index_input(self, value):
        if not value.isdigit():
            raise InvalidInputException()

        value = int(value)
        if value < 0 or value >= self.board.size:
            raise InvalidInputException()  # TODO: Specific exception type

        return value

    @staticmethod
    def _convert_value_to_display(value):
        return str(CELL_DISPLAY_MAP.get(value, value))
