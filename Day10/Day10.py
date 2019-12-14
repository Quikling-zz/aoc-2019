from collections import defaultdict
from math import gcd, atan


def get_slope(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    del_x, del_y = x2 - x1, y2 - y1
    den = gcd(del_x, del_y)
    return del_x // den, del_y // den


def part1(file_name):
    with open(file_name, 'r') as input_file:
        field = defaultdict(lambda: defaultdict(int))
        for y, line in enumerate(input_file.readlines()):
            for x, elem in enumerate(line):
                field[y][x] = elem

    asteroids = []
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == '#':
                asteroids.append((x, y))

    max_seen = (0, (0, 0))
    for i, baseteroid in enumerate(asteroids):
        slopes = set()
        for j, asteroid in enumerate(asteroids):
            if i != j:
                slopes.add(get_slope(baseteroid, asteroid))

        max_seen = max(max_seen, (len(slopes), baseteroid), key=lambda a: a[0])

    print(max_seen)

    return max_seen, field


def part2(file_name):
    (num, max_asteroid), field = part1(file_name)
    from_end = num - 200

    asteroids = set()
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[y][x] == '#' and (x, y) != max_asteroid:
                slope = get_slope(max_asteroid, (x, y))
                asteroids.add(slope)

    filtered = []
    for asteroid in asteroids:
        if asteroid[0] < 0:
            theta = atan(asteroid[1] / asteroid[0])
            filtered.append((asteroid[0], asteroid[1], theta))

    filtered.sort(key=lambda a: a[2], reverse=True)

    print(filtered)
    del_x, del_y = filtered[from_end][:2]
    print(filtered[from_end])

    print(del_x, del_y)
    y_coord = del_y + max_asteroid[1]
    x_coord = del_x + max_asteroid[0]
    print(field[y_coord][x_coord])

    print(x_coord, y_coord)


if __name__ == '__main__':
    part2('input.txt')
