# day 11 of AOC23

import fileinput

filename = 'day11_input.txt'

#puzzle 1
#inserts a physical colums into an expanend_input array
def add_col(col):
    for i in range(len(expanded_input)):
        expanded_input[i].insert(col, '.')

#parse original input into an array
input = []
for line in fileinput.input(files = filename):
    arr = []
    for e in line.strip():
        arr.append(e)
    input.append(arr)

#expand input, modify by inserting rows and columns accordingly
expanded_input = []
index = 0

#insert rows
for line in input:
    if '#' not in line:
        expanded_input.insert(index, ['.' for i in range(len(line))])
        index+=1
    expanded_input.insert(index, line.copy())
    index+=1

#insert colums
index = 0
end = len(expanded_input[0])
while index < end:
    boo = True
    for i in range(len(expanded_input)):
        if expanded_input[i][index] == '#': boo = False
    if boo: 
        add_col(index)
        index+=1
        end += 1
    index+=1

#label galaxies with numbers
no_galaxy = 1
indicies = []
for i in range(len(expanded_input)):
    for j in range(len(expanded_input[i])):
        if expanded_input[i][j]=='#': 
            expanded_input[i][j] = no_galaxy
            no_galaxy+=1
            indicies.append([i, j])

#go through galaxies and sum up their distances
tot_dist = 0
for i in range(len(indicies)):
    for j in range(i+1, len(indicies), 1):
        #formula to get min distance
        tot_dist += abs(indicies[i][0]-indicies[j][0]) + abs(indicies[i][1]-indicies[j][1])
print(tot_dist)

#puzzle 2
#work if original input
#arrays to collect indicies of empty colums and rows
exp_rows = []
exp_cols = []

#get indicies of emtpy rows
for i in range(len(input)):
    if '#' not in input[i]:
        exp_rows.append(i)

#get indicies of emtpy colums
for j in range(len(input[0])):
    boo = True
    for i in range(len(input)):
        if input[i][j] == '#': boo = False
    if boo: 
        exp_cols.append(j)

#label galaxies
no_galaxy = 1
indicies = []
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j]=='#': 
            input[i][j] = no_galaxy
            no_galaxy+=1
            indicies.append([i, j])

#count min distances, for crossing an expanded row/col count millions +1
tot_dist = 0
millions = 0
for i in range(len(indicies)):
    for j in range(i+1, len(indicies), 1):
        tot_dist += abs(indicies[i][0]-indicies[j][0]) + abs(indicies[i][1]-indicies[j][1])
        #check for crossed expanded rows/cols
        for k in range(min(indicies[i][0], indicies[j][0]), max(indicies[i][0], indicies[j][0]), 1):
            if k in exp_rows: millions+=1
        for m in range(min(indicies[i][1], indicies[j][1]), max(indicies[i][1], indicies[j][1]), 1):
            if m in exp_cols: millions+=1
print(tot_dist+millions*999999)