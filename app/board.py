from typing import Generator, Tuple, List
from random import randrange


FLAG = -1
BOMB = -2


class Board:
    def __init__(self, size: int, num_of_bombs: int):
        self.size = size
        self.num_of_bombs = num_of_bombs
        self.num_of_exposed = 0
        self.num_of_flags = 0
        self.bomb_exposed = False
        self.all_exposed = False

        self.exposed = self._get_filled_matrix(None)
        self._bombs = self._get_filled_matrix(False)

        self._set_bombs()

    def set_flag(self, row: int, column: int) -> None:
        cell_value = self.exposed[row][column]
        if cell_value != None and cell_value != FLAG:
            return

        value = None if cell_value else FLAG

        self._update(row, column, value)

    def expose(self, row: int, column: int) -> None:
        if self.exposed[row][column] != None:
            return

        value = BOMB if self._bombs[row][column] else self._calculate_cell(row, column)
        self._update(row, column, value)

        # Relveal obvious cells
        if value == 0:
            for i, j in self._iterate_block(row, column):
                self.expose(i, j)

    def expose_bombs(self) -> None:
        for i in range(self.size):
            for j in range(self.size):
                if self._bombs[i][j] and not self.exposed[i][j]:
                    self._update(i, j , BOMB)

    def _update(self, row: int, column: int, value: int) -> None:
        old = self.exposed[row][column]
        self.exposed[row][column] = value

        if old != value:
            sign = 1 if old is None else -1
            self.num_of_exposed += sign
            self.num_of_flags += ((old or value) == FLAG) * sign
            self.all_exposed = self.num_of_exposed == self.size * self.size
            self.bomb_exposed = value == BOMB

    def _calculate_cell(self, row: int, column: int) -> int:
        count = 0
        for i, j in self._iterate_block(row, column):
            if self._bombs[i][j]:
                count += 1

        return count

    def _iterate_block(self, row: int, column: int) -> Generator[Tuple[int, int], None, None]:
        starting_row = max(row - 1, 0)
        starting_column = max(column - 1, 0)
        ending_row = min(row + 1, self.size - 1)
        ending_column = min(column + 1, self.size - 1)

        for i in range(starting_row, ending_row + 1):
            for j in range(starting_column, ending_column + 1):
                yield i, j

    def _set_bombs(self) -> None:
        for i in range(self.num_of_bombs):
            row, column = randrange(self.size), randrange(self.size)
            while self._bombs[row][column]:
                row, column = randrange(self.size), randrange(self.size)

            self._bombs[row][column] = True

    def _get_filled_matrix(self, fill_value):
        return [
            [fill_value] * self.size
            for i in range(self.size)
        ]
