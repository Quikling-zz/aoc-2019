from shared.OpCoder import OpCoder
from queue import Queue
from collections import defaultdict
from subprocess import call
from time import sleep


class Board:
    def __init__(self):
        self.board = defaultdict(lambda: defaultdict(lambda: ' '))
        self.score = 0
        self.ball = 0
        self.paddle = 0

    def update_board(self, x, y, tile):
        if x == -1:
            self.score = tile
        elif tile == 0:
            self.board[y][x] = ' '
        elif tile == 1:
            self.board[y][x] = '█'
        elif tile == 2:
            self.board[y][x] = '░'
        elif tile == 3:
            self.board[y][x] = '─'
            self.paddle = x
        elif tile == 4:
            self.board[y][x] = '©'
            self.ball = x
        else:
            print('derp')

    def print_board(self):
        call('clear')
        # print('\n' * 40)
        for i in range(0, 26):
            line = []
            for j in range(0, 46):
                line.append(self.board[i][j])
            print(''.join(line))
        print(self.score)

    def get(self):
        return 0 if self.ball == self.paddle else 1 if self.ball > self.paddle else -1


def get_input(file_name):
    with open(file_name, 'r') as input_file:
        op_codes = list(map(int, input_file.read().split(',')))
    return op_codes


def part1(op_codes):
    op_coder = OpCoder(op_codes)

    blocks = 0
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    while not op_coder.halt:
        x = op_coder.run()
        y = op_coder.run()
        tile = op_coder.run()

        if x is not None and y is not None:
            x_min = min(x, x_min)
            y_min = min(y, y_min)
            x_max = max(x, x_max)
            y_max = max(y, y_max)

        if tile == 2:
            blocks += 1

    print(blocks)
    print(x_min, x_max, y_min, y_max)


def part2(op_codes):
    op_codes[0] = 2
    board = Board()
    op_coder = OpCoder(op_codes, board)

    for _ in range(1195):
        x = op_coder.run()
        y = op_coder.run()
        tile = op_coder.run()
        board.update_board(x, y, tile)

    board.print_board()
    sleep(10)

    while not op_coder.halt:
        # sleep(.01)
        x = op_coder.run()
        y = op_coder.run()
        tile = op_coder.run()
        board.update_board(x, y, tile)
        board.print_board()


if __name__ == '__main__':
    op_code_list = get_input('input.txt')
    part1(op_code_list)
    part2(op_code_list)
