""" Solutions for Day 1  """
import sys

infile = open(sys.argv[1], "r")

r_sum = 0

for mass in infile:
    massAsInt = int(mass)
    r_sum += (massAsInt//3)-2

print(r_sum)


infile.close()
