# day 9 of AOC23

import fileinput

filename = 'day9_input.txt'

#puzzle 1
#make input: array of histories 
input = []
for line in fileinput.input(files = filename):
    input.append(line.strip().split())

sum = 0
#save the intermediates differences of each history in an array of arrays of arrays
diff = []
for i in input:
    differences = []
    arr = i
    differences.append(arr)
    #get intermediate differences of current history
    while set(arr) != {0}:
        arr_help = []
        #execute one step of differences
        for j in range(len(arr)-1):
            arr_help.append(int(arr[j+1])-int(arr[j]))
        differences.append(arr_help)
        arr = arr_help
    #go over intermediate differences of current history and add up the last element of each intermediate
    for k in range(len(differences)-1, -1, -1):
        sum += int(differences[k][-1])
    diff.append(differences)

print(sum)

#puzzle 2
sum = 0
for d in diff:
    #memorize the value to subtract in the next step
    sub = 0
    for k in range(len(d)-1, -1, -1):
        #go over the first element of each intermediate step of each history to get new value for sub
        sub = int(d[k][0]) - sub
    #for each history sum up current sub
    sum += sub

print(sum)