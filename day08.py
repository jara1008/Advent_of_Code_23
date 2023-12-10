# day 8 of AOC23

import fileinput
import math
from functools import reduce 

filename = 'day8_input.txt'

#puzzle 1
def count_step(begin, end, directions, starts):
    i = 0
    no_steps = 0
    while begin not in end:
        index = -1
        for k in range(len(starts)):
            if starts[k] == begin:
                index = k
        if directions[i] == 'L':
            begin = l[index]
        elif directions[i] == 'R':
            begin = r[index]
        i += 1
        if i == len(directions):
            i = 0
        no_steps += 1
    return no_steps


starts = []
l = []
r = []

row = 0
directions = []
for line in fileinput.input(files = filename):
    if row == 0:
        for e in line.strip():
            directions.append(e)
        row += 1
        continue
    if row == 1:
        row += 1
        continue
    for i in range(len(line)):
        if i==0:
            starts.append(line[0: 3])
        if i==7:
            l.append(line[7: 10])
        if i == 12:
            r.append(line[12: 15])

begin = 'AAA' 
end = 'ZZZ'       

print(count_step(begin, end, directions, starts))

#puzzle 2
begin = []
ends = []
for e in starts:
    if e[2] == 'A':
        begin.append(e)
    if e[2] == 'Z':
        ends.append(e)

no_steps = []
for num in begin:
    no_steps.append(count_step(num, ends, directions, starts))

print(reduce(math.lcm, no_steps))




