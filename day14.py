# day 14 of AOC23

import fileinput

filename = 'day14_input.txt'

#puzzle 1
def roll_north():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]=='O':
                index = i-1
                while index >= 0 and lines[index][j]=='.':
                    lines[index][j]='O'
                    lines[index+1][j]='.'
                    index-=1

#make input grid
lines = []
for line in fileinput.input(files = filename):
    arr_help = []
    for e in line.strip():
        arr_help.append(e)
    lines.append(arr_help)

#take one turn north
roll_north()

#add up accordingly 
total = 0
line = 1
for i in range(len(lines)-1, -1, -1):
    for j in range(len(lines[0])):
        if lines[i][j]=='O': total += line
    line+=1
print(total)

#puzzle 2
def roll_west():
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j]=='O':
                index = j-1
                while index >= 0 and lines[i][index]=='.':
                    lines[i][index]='O'
                    lines[i][index+1]='.'
                    index-=1

def roll_south():
    for i in range(len(lines)-1, -1, -1):
        for j in range(len(lines[0])):
            if lines[i][j]=='O':
                index = i+1
                while index < len(lines) and lines[index][j]=='.':
                    lines[index][j]='O'
                    lines[index-1][j]='.'
                    index+=1

def roll_east():
    for i in range(len(lines)):
        for j in range(len(lines[0])-1, -1, -1):
            if lines[i][j]=='O':
                index = j+1
                while index < len(lines[0]) and lines[i][index]=='.':
                    lines[i][index]='O'
                    lines[i][index-1]='.'
                    index+=1

#remember patterns already seen
patterns = []

#finish 1st cycle
roll_west()
roll_south()
roll_east()
patterns.append([i.copy() for i in lines])

#track how many cycles already done
track = 1
for i in range(1000000000):
    #take turn
    roll_north()
    roll_west()
    roll_south()
    roll_east()
    #if there is a pattern break the loop
    if lines in patterns: break
    #else remember current pattern
    patterns.append([i.copy() for i in lines])
    track+=1

#get index of pattern in patterns two know how long the loop is between equal patterns
start = patterns.index(lines)
#track-start => length of loop, 1000000000-start => amount of cycles that are 'in loops'
#(1000000000-start)%(track-start) => index where we exit the loop
sol_pattern = patterns[(1000000000-start)%(track-start)+start-1]

#add up accordingly
total = 0
line = 1
for i in range(len(sol_pattern)-1, -1, -1):
    for j in range(len(sol_pattern[0])):
        if sol_pattern[i][j]=='O': total += line
    line+=1

print(total)