from timeit import default_timer as timer


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '({}, {})'.format(self.x, self.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def man_dist(self):
        return abs(self.x) + abs(self.y)

    def get_coord(self):
        return Point(self.x, self.y)


def get_unit_vec(direction):
    if direction == 'U':
        return Point(0, 1)
    elif direction == 'R':
        return Point(1, 0)
    elif direction == 'L':
        return Point(-1, 0)
    else:
        return Point(0, -1)


def get_input():
    wire_moves = []
    with open('input.txt', 'r') as f:
        for wire in f.readlines():
            wire_moves.append(wire.split(','))
    return wire_moves


def part1():
    wire_a_moves, wire_b_moves = get_input()

    total_dist = 0
    curr_coord = Point(0, 0)
    a_coords = dict()
    for move in wire_a_moves:
        direction = get_unit_vec(move[0])
        distance = int(move[1:])
        for _ in range(distance):
            total_dist += 1
            curr_coord + direction
            if curr_coord not in a_coords:
                a_coords[curr_coord.get_coord()] = total_dist

    total_dist = 0
    curr_coord = Point(0, 0)
    intersections = dict()
    for move in wire_b_moves:
        direction = get_unit_vec(move[0])
        distance = int(move[1:])
        for _ in range(distance):
            total_dist += 1
            curr_coord + direction
            if curr_coord in a_coords and curr_coord not in intersections:
                intersections[curr_coord.get_coord()] = total_dist + a_coords[curr_coord]

    closest_sig = min(intersections, key=lambda p: intersections[p])
    closest_man = min(intersections, key=lambda p: p.man_dist())
    print(closest_man, closest_man.man_dist())
    print(closest_sig, intersections[closest_sig])


if __name__ == '__main__':
    start = timer()
    part1()
    end = timer()
    print('time: {}'.format(end - start))
