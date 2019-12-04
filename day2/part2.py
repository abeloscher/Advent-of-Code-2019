""" """
import sys
import itertools
import copy

def chunk_list(_list, size):
    for i in range(0, len(_list), size):
        yield _list[i:i + size]


def calc_pos(pos):
    return {
        'x': (pos % 4),
        'y': (pos // 4)
    }


def find_value(pos, chunked_list):
    coords = calc_pos(pos)
    return int(chunked_list[coords['y']][coords['x']])


def parse(chunked_list):
    for _list in chunked_list:
        opcode = int(_list[0])
        out_pos = calc_pos(int(_list[3]))

        if opcode == 1:
            res = find_value(int(_list[1]), chunked_list) + find_value(int(_list[2]), chunked_list)
            chunked_list[out_pos['y']][out_pos['x']] = res
        elif opcode == 2:
            res = find_value(int(_list[1]), chunked_list) * find_value(int(_list[2]), chunked_list)
            chunked_list[out_pos['y']][out_pos['x']] = res
        else:
            return int(chunked_list[0][0])


infile = open(sys.argv[1], "r")

for line in infile:
    _list = line.split(",")
    bounds = list(range(0, 100))
    permutations = [p for p in itertools.product(bounds, repeat=2)]
    chunked = list(chunk_list(_list, 4))
    for entry in permutations:
        chunked_copy = copy.deepcopy(chunked)
        chunked_copy[0][1] = entry[0]
        chunked_copy[0][2] = entry[1]
        result = parse(chunked_copy)
        if result == 19690720:
            print(entry)
            print(result)
            exit(0)
infile.close()
