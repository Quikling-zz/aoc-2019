from copy import deepcopy


def part1():
    with open('input1.txt', 'r') as input:
        opcodes = list(map(int, input.read().split(',')))

    opcodes[1] = 12
    opcodes[2] = 2

    opcoder(opcodes)


def opcoder(opcodes):
    for i in range(0, len(opcodes), 4):
        opcode = opcodes[i]
        if opcode == 1 or opcode == 2:
            src1 = opcodes[i + 1]
            src2 = opcodes[i + 2]
            dest = opcodes[i + 3]
            if opcode == 1:
                opcodes[dest] = opcodes[src1] + opcodes[src2]
            else:
                opcodes[dest] = opcodes[src1] * opcodes[src2]
        elif opcodes[i] == 99:
            return opcodes[0]
        else:
            return -1


def part2():
    target = 19690720

    with open('input1.txt', 'r') as input :
        opcodes = list(map(int, input.read().split(',')))

    initial_state = deepcopy(opcodes)

    for noun in range(100):
        for verb in range(100):
            opcodes = deepcopy(initial_state)
            opcodes[1] = noun
            opcodes[2] = verb
            if opcoder(opcodes) == target:
                return 100 * noun + verb


if __name__ == '__main__':
    part1()
    part2()
