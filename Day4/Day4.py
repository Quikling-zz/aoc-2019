from time import time


def inc_list_num(num_list):
    num_list.reverse()
    num_list[0] += 1
    for i in range(5):
        if num_list[i] == 10:
            num_list[i] = 0
            num_list[i + 1] += 1        
    num_list.reverse()
    if 0 in num_list:
        num_list = get_next_increasing(num_list)
    return num_list


def get_next_increasing(num_list):
    last = 0
    increasing = True
    for i, num in enumerate(num_list):
        if num >= last:
            last = num
        else:
            increasing = False
            for j in range(6 - i):
                num_list[i + j] = last
            break
            
    if increasing:
        num_list = inc_list_num(num_list)

    return num_list


def check_doubles(num_list):
    last = 0
    count = 0
    counts = []
    for num in num_list:
        if num == last:
            count += 1
        else:
            counts.append(count)
            count = 0
            last = num
    counts.append(count)
    return 1 in counts


def part1():
    curr = list(map(int, str(231832)))
    end = list(map(int, str(767346)))

    total = 0
    while curr < end:
        if check_doubles(curr):
            total += 1
        curr = get_next_increasing(curr)

    print(total)
        

if __name__ == '__main__':
    start = time()
    part1()
    end = time()
    print(end - start)
