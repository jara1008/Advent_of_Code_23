# day 22 of AOC23

import fileinput

filename = 'day22_input.txt'

#puzzle 1
def drop(brick, tower):
    is_empty = True
    while is_empty and brick[0][2] > 1:
        for i in range(brick[0][0], brick[1][0]+1):
            for j in range(brick[0][1], brick[1][1]+1):
                if tower[i][j][brick[0][2]-1]:
                    is_empty=False
        if is_empty:
            brick = [(brick[0][0], brick[0][1], brick[0][2]-1), (brick[1][0], brick[1][1], brick[1][2]-1)]
    return brick

def drop_check(brick, tower):
    is_empty = brick[0][2]>1
    for i in range(brick[0][0], brick[1][0]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            if tower[i][j][brick[0][2]-1]:
                is_empty=False
    return is_empty

def set_in_tower(brick, tower):
    for i in range(brick[0][0], brick[1][0]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            for k in range(brick[0][2], brick[1][2]+1):
                tower[i][j][k]=True

def unset_in_tower(brick, tower):
    for i in range(brick[0][0], brick[1][0]+1):
        for j in range(brick[0][1], brick[1][1]+1):
            for k in range(brick[0][2], brick[1][2]+1):
                tower[i][j][k]=False

bricks = []
for line in fileinput.input(files = filename):
    nums = line.split('~')
    brick = []
    begin = tuple(map(int, nums[0].split(',')))
    end = tuple(map(int, nums[1].strip().split(',')))
    brick.append(begin)
    brick.append(end)
    bricks.append(brick)
bricks.sort(key=lambda x: x[0][2])

tower = []
for i in range(10):
    y=[]
    for j in range(10):
        z=[]
        for k in range(500):
            z.append(False)
        y.append(z)
    tower.append(y)

dropped_bricks = []
for i in range(len(bricks)):
    bricks[i] = drop(bricks[i], tower)
    dropped_bricks.append(bricks[i])
    set_in_tower(bricks[i], tower)

unsafe_bricks=[]
for i in range(len(dropped_bricks)):
    unset_in_tower(dropped_bricks[i], tower)
    for j in range(i+1, len(dropped_bricks)):
        if drop_check(dropped_bricks[j], tower): 
            unsafe_bricks.append(dropped_bricks[i])
            break
    set_in_tower(dropped_bricks[i], tower)
print(len(dropped_bricks)-len(unsafe_bricks))

#puzzle 2
total = 0
for i in range(len(unsafe_bricks)):
    count=0
    dropped=[]
    dropped.append(unsafe_bricks[i])
    unset_in_tower(unsafe_bricks[i], tower)
    for j in range(dropped_bricks.index(unsafe_bricks[i])+1, len(dropped_bricks)):
        if drop_check(dropped_bricks[j], tower): 
            count += 1
            unset_in_tower(dropped_bricks[j], tower)
            dropped.append(dropped_bricks[j])
    for b in dropped:
        set_in_tower(b, tower)
    total += count
print(total)