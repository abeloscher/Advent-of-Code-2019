""" """
import sys


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
    chunked_list = list(chunked_list)
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
            print(chunked_list[0][0])
            exit(0)


infile = open(sys.argv[1], "r")

for line in infile:
    _list = line.split(",")
    parse(list(chunk_list(_list, 4)))

infile.close()
