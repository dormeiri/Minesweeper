from board import Board, FLAG, BOMB
from colorama import Fore, Style


SEPERATOR = '\t'
CELL_DISPLAY_MAP = {
    FLAG: Fore.GREEN + 'F',
    None: Fore.WHITE + '-',
    BOMB: Fore.RED + '*'
}


class InvalidInputException(Exception):
    pass


class Console:
    def __init__(self, board: Board):
        self.board = board

    def print_status(self):
        print(f'Flags: {self.board.num_of_bombs - self.board.num_of_flags}')

    def print_end(self, game_over):
        self.board.expose_bombs()
        self.show_board()

        print('Game over!' if game_over else 'You won!')

    def show_board(self):
        print('\n ', end='\t')
        print(*range(self.board.size), sep=SEPERATOR, end='\n\n')

        for i in range(self.board.size):
            row = self.board.exposed[i]
            row_display = map(Console._convert_value_to_display, row)

            print(i, end='\t')
            print(*row_display, sep=SEPERATOR)

        print(Style.RESET_ALL)

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
            raise InvalidInputException()

        return value

    @staticmethod
    def _convert_value_to_display(value):
        return str(CELL_DISPLAY_MAP.get(value, Fore.WHITE + str(value)))
