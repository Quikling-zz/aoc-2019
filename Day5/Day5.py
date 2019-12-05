from shared.OpCoder import OpCoder


def part1():
    with open('input.txt', 'r') as input_file:
        op_codes = list(map(int, input_file.read().split(',')))

    op_coder = OpCoder(op_codes)
    op_coder.run()


if __name__ == '__main__':
    part1()
