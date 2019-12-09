from itertools import permutations
from queue import Queue
from time import time

from shared.OpCoder import OpCoder


def part1():
    with open('input.txt', 'r') as input_file:
        op_codes = list(map(int, input_file.read().split(',')))

    max_out = 0
    queue = Queue()

    for perm in permutations(range(5, 10)):
        op_coders = [OpCoder(op_codes.copy(), queue) for _ in perm]
        output = 0
        for i, phase in enumerate(perm):
            queue.put(phase)
            queue.put(output)
            output = op_coders[i].run()

        i = 0
        while not any(coder.halt for coder in op_coders):
            queue.put(output)
            output = op_coders[i % 5].run()
            i += 1

        max_out = max(queue.get(), max_out)

    print(max_out)


if __name__ == '__main__':
    start = time()
    part1()
    end = time()
    print('Time: {}'.format(end - start))
