# day 10 of AOC23

import fileinput

filename = 'day10_input.txt'    

#puzzle 1
def get_index(i, j, from_dir):
    if input[i-1][j] in '|F7S' and from_dir != 1 and input[i][j] in 'J|LS':
        return [i-1, j, 3]
    elif input[i+1][j] in '|JLS' and from_dir != 3 and input[i][j] in 'F|7S':
        return [i+1, j, 1]
    elif input[i][j-1] in '-FLS' and from_dir != 4 and input[i][j] in '-J7S':
        return [i, j-1, 2]
    elif input[i][j+1] in '-J7S' and from_dir != 2 and input[i][j] in '-FLS':
        return [i, j+1, 4]
    else: print('ERROR')

input = []
length = 0
first = True
start_i = -1
start_j = -1
i = 1

for line in fileinput.input(files = filename):
    j = 1
    arr = []
    arr.append('.')
    for e in line.strip():
        arr.append(e)
        if first: length += 1
        if e == 'S':
            start_i = i
            start_j = j
        j += 1
    arr.append('.')
    input.append(arr)
    first = False
    i += 1

input.append(['.' for i in range(length+2)])
input.insert(0, ['.' for i in range(length+2)])

input_X = [e.copy() for e in input]
input_X[start_i][start_j] = 'X'

help_arr = get_index(start_i, start_j, 0)
curr_i = help_arr[0]
curr_j = help_arr[1]
from_dir = help_arr[2]
input_X[curr_i][curr_j] = 'X'

count_steps = 1
while input[curr_i][curr_j] != 'S':
    help_arr = get_index(curr_i, curr_j, from_dir)
    curr_i = help_arr[0]
    curr_j = help_arr[1]
    from_dir = help_arr[2]
    input_X[curr_i][curr_j] = 'X'
    count_steps += 1

print(int(count_steps/2))

#puzzle 2
#in the previous loop we replaced all elements belonging to the pipe with 'X' in a copy of input
expanded_input = []

for i in range(len(input_X)):
    line1 = ''
    line2 = ''
    line3 = ''
    for j in range(len(input_X[0])):
        if input_X[i][j] == 'X':
            if input[i][j] == '-':
                line1 += '   '
                line2 += 'XXX'
                line3 += '   '
            elif input[i][j] == '|':
                line1 += ' X '
                line2 += ' X '
                line3 += ' X '
            elif input[i][j] == 'F':
                line1 += '   '
                line2 += ' XX'
                line3 += ' X '
            elif input[i][j] == 'L':
                line1 += ' X '
                line2 += ' XX'
                line3 += '   '
            elif input[i][j] == 'J':
                line1 += ' X '
                line2 += 'XX '
                line3 += '   '
            elif input[i][j] == '7':
                line1 += '   '
                line2 += 'XX '
                line3 += ' X '
            elif input[i][j] == 'S':
                if input[i-1][j] in "F7|":
                    line1 += ' X '
                    if input[i][j-1] in "F-L":
                        line2 += 'XX '
                        line3 += '   '
                    elif input[i+1][j] in "J|L":
                        line2 += ' X '
                        line3 += ' X '
                    else:
                        line2 += ' XX'
                        line3 += '   '          
                elif input[i+1][j] in "J|L":
                    line3 += ' X '
                    if input[i][j-1] in "F-L":
                        line2 += 'XX '
                        line1 += '   '
                    else:
                        line2 += ' XX'
                        line1 += '   ' 
                else:
                    line1 += '   '
                    line2 += 'XXX'
                    line3 += '   '
        else:
            line1 += '   '
            line2 += '   '
            line3 += '   '
    expanded_input.append(list(line1))
    expanded_input.append(list(line2))
    expanded_input.append(list(line3))

for i in range(len(expanded_input)):
    j=0
    pr = False
    while j<len(expanded_input[0]):
        if expanded_input[i][j]=="X":
            a = expanded_input[i-1][j] + expanded_input[i+1][j]
            while expanded_input[i][j]=="X": j+=1
            b = expanded_input[i-1][j-1] + expanded_input[i+1][j-1]
            if a[0]=="X"==b[1] or a[1]=="X"==b[0]:
                pr = not pr
            j=j-1
        elif pr:
            expanded_input[i][j]="I"
        j+=1

count = 0
for i in range(1, len(expanded_input), 3):
    for j in range(1, len(expanded_input[i]), 3):
        if expanded_input[i][j] == 'I': count += 1

print(count)