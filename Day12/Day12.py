from itertools import combinations


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.x_vel = 0
        self.y_vel = 0
        self.z_vel = 0

    def __repr__(self):
        return 'Position: <{}, {}, {}> Velocity: <{}, {}, {}>'.format(self.x, self.y, self.z,
                                                                      self.x_vel, self.y_vel, self.z_vel)

    def update_vel(self, other):
        self.x_vel += 0 if self.x == other.x else (1 if self.x < other.x else -1)
        self.y_vel += 0 if self.y == other.y else (1 if self.y < other.y else -1)
        self.z_vel += 0 if self.z == other.z else (1 if self.z < other.z else -1)

    def update_pos(self):
        self.x += self.x_vel
        self.y += self.y_vel
        self.z += self.z_vel

    def get_energy(self):
        return sum(map(abs, [self.x, self.y, self.z])) * sum(map(abs, [self.x_vel, self.y_vel, self.z_vel]))

    def __eq__(self, other):
        x_bool = self.x == other.x
        y_bool = self.y == other.y
        z_bool = self.z == other.z
        x_vel_bool = self.x_vel == other.x_vel
        y_vel_bool = self.y_vel == other.y_vel
        z_vel_bool = self.z_vel == other.z_vel

        return x_bool and y_bool and z_bool and x_vel_bool and y_vel_bool and z_vel_bool


def read_input(file_name):
    with open(file_name, 'r') as input_file:
        moons = []
        for line in input_file.read().splitlines():
            start_pos = list(map(lambda pos: int(pos.split('=')[1]), line[:-1].split(',')))
            moons.append(Moon(start_pos[0], start_pos[1], start_pos[2]))
    return moons


def part1(file_name):
    moons = read_input(file_name)
    start_moons = read_input(file_name)

    print(all(moon == start_moons[i] for i, moon in enumerate(moons)))

    count = 0
    for _ in range(2775):
        count += 1
        for moon1, moon2 in combinations(moons, 2):
            moon1.update_vel(moon2)
            moon2.update_vel(moon1)

        for moon in moons:
            moon.update_pos()

        if all(moon == start_moons[i] for i, moon in enumerate(moons)):
            break

    for i, moon in enumerate(moons):
        print(moon)
        print(start_moons[i])
        print()

    print('Energy: {}'.format(sum(map(lambda m: m.get_energy(), moons))))
    print(count)


if __name__ == '__main__':
    part1('test2.txt')
