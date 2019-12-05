def part1():
    total = 0
    with open('input1.txt', 'r') as input:
        for module in input.readlines():
            total += int(module) // 3 - 2
    return total


def part2():
    total = 0
    with open('input1.txt', 'r') as input:
        for module_weight in input.readlines():
            inc_fuel = int(module_weight) // 3 - 2
            while inc_fuel > 0:
                total += inc_fuel
                inc_fuel = inc_fuel // 3 - 2
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
