from board import Board
from game_manager import GameManager


def main():
    size = int(input('Board size: '))
    num_of_bombs = int(input('Number of bombs: '))

    board = Board(size, num_of_bombs)
    game_manager = GameManager(board)

    game_manager.run()


if __name__ == '__main__':
    main()
