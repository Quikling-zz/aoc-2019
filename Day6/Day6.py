from collections import defaultdict
from queue import Queue


def part1():
    with open('input.txt', 'r') as input_file:
        orbits = map(lambda o: o.split(')'), input_file.read().splitlines())

    orbit_graph = defaultdict(set)
    for center, mass in orbits:
        orbit_graph[center].add(mass)

    total = 0
    queue = Queue()
    queue.put((orbit_graph['COM'], 1))
    while not queue.empty():
        orbiters, depth = queue.get()
        for orbiter in orbiters:
            total += depth
            queue.put((orbit_graph[orbiter], depth + 1))

    print(total)


def part2():
    with open('input.txt', 'r') as input_file:
        orbits = map(lambda o: o.split(')'), input_file.read().splitlines())

    orbit_graph = defaultdict(set)
    for center, mass in orbits:
        orbit_graph[center].add(mass)
        orbit_graph[mass].add(center)

    visited = set()
    queue = Queue()
    queue.put((orbit_graph['YOU'], -1))
    while not queue.empty():
        orbiters, depth = queue.get()
        if 'SAN' in orbiters:
            print(depth)
            return
        else:
            for orbiter in orbiters:
                if orbiter not in visited:
                    visited.add(orbiter)
                    queue.put((orbit_graph[orbiter], depth + 1))


if __name__ == '__main__':
    part1()
    part2()
