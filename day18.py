# day 18 of AOC23

import fileinput

filename = 'day18_input.txt'

#puzzle 1
def go_R(field, i, j, num):
    for k in range(num):
        field[i][j+k]='#'
    return j+num

def go_L(field, i, j, num):
    for k in range(num):
        field[i][j-k]='#'
    return j-num

def go_D(field, i, j, num):
    for k in range(num):
        field[i+k][j]='#'
    return i+num

def go_U(field, i, j, num):
    for k in range(num):
        field[i-k][j]='#'
    return i-num

inputs = []
for line in fileinput.input(files = filename):
    inputs.append(line.strip().split())

row = ['.' for i in range(800)]
field = [row.copy() for i in range(800)]
curr_i = int(len(field)/2)
curr_j = int(len(field[0])/2)

for tup in inputs:
    d = tup[0]
    num = int(tup[1])
    if d=='R': 
        curr_j=go_R(field, curr_i, curr_j, num)
    elif d=='L':
        curr_j=go_L(field, curr_i, curr_j, num)
    elif d=='D':
        curr_i=go_D(field, curr_i, curr_j, num)
    elif d=='U':
        curr_i=go_U(field, curr_i, curr_j, num)

total = 0
for i in range(len(field)):
    j=0
    pr = False
    while j<len(field[0]):
        if field[i][j]=="#":
            a = field[i-1][j] + field[i+1][j]
            while field[i][j]=="#": j+=1
            b = field[i-1][j-1] + field[i+1][j-1]
            if a[0]=="#"==b[1] or a[1]=="#"==b[0]:
                pr = not pr
            j=j-1
        elif pr:
            total+=1
        j+=1

for i in range(len(field)):
    for j in range(len(field[0])):
        if field[i][j]=='#': total+=1
 
print(total)

#puzzle 2
d = []
nums = []
for tup in inputs:
    instr = tup[2][2:-1]
    dir = instr[-1]
    if dir=='0': d.append('R')
    if dir=='1': d.append('D')
    if dir=='2': d.append('L')
    if dir=='3': d.append('U')
    nums.append(int(instr[:-1], base=16))

x = 0
y = 0
total = 1
for i in range(len(d)):
    if d[i]=='R':
        y+=nums[i]
        total+=nums[i]
    if d[i]=='D':
        x+=nums[i]
        total+=nums[i]*y
    if d[i]=='L':
        y-=nums[i]
    if d[i]=='U':
        x-=nums[i]
        total-=nums[i]*(y-1)
print(total)