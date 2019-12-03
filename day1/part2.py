""" Solutions for Day 1  """
import sys


def calc_til_0(mass: int):
    r_sum = 0
    while (mass//3)-2 > 0:
        mass = mass//3-2
        r_sum += mass
    return r_sum


def calc_til_0_recurse_step(mass: int):

    if mass <= 0:
        return 0
    return mass + calc_til_0_recurse_step((mass//3)-2)


def calc_til_0_call_recurse(mass: int):
    return calc_til_0_recurse_step(mass) - mass


infile = open(sys.argv[1], "r")

r_sum = 0

for mass in infile:
    massAsInt = int(mass)
    r_sum += calc_til_0_call_recurse(massAsInt)

print(r_sum)

infile.close()
