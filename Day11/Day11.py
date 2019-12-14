from shared.OpCoder import OpCoder
from shared.Point import Point
from collections import defaultdict
from queue import Queue
from PIL import Image

import numpy as np


def get_unit_vec(direction):
    if direction == 0:
        return Point(0, 1)
    elif direction == 1:
        return Point(1, 0)
    elif direction == 3:
        return Point(-1, 0)
    else:
        return Point(0, -1)


def part1(file_name):
    with open(file_name, 'r') as input_file:
        op_codes = list(map(int, input_file.read().split(',')))

    hull_map = defaultdict(int)
    coords = Point(0, 0)
    direction = 0

    queue = Queue()
    op_coder = OpCoder(op_codes.copy(), queue)

    queue.put(1)

    painted = set()
    while not op_coder.halt:
        paint = op_coder.run()
        turn = op_coder.run()
        if paint is None:
            break
        direction = direction + 1 if turn == 1 else direction - 1
        direction %= 4

        curr_coord = Point(coords.x, coords.y)
        hull_map[curr_coord] = paint
        painted.add(curr_coord)
        unit_vec = get_unit_vec(direction)
        coords = Point(coords.x + unit_vec.x, coords.y + unit_vec.y)
        queue.put(hull_map[coords])

    print(len(painted))

    x_max = max(hull_map.keys(), key=lambda x: x.x).x
    x_min = min(hull_map.keys(), key=lambda x: x.x).x

    y_max = max(hull_map.keys(), key=lambda x: x.y).y
    y_min = min(hull_map.keys(), key=lambda x: x.y).y

    out_map = np.zeros((y_max - y_min + 1, x_max - x_min + 1))

    for i in range(len(out_map)):
        for j in range(len(out_map[0])):
            out_map[i][j] = hull_map[Point(j, i - 5)]

    img = Image.fromarray(np.uint8(out_map*255))
    img.save('derp.png')


if __name__ == '__main__':
    part1('input.txt')
