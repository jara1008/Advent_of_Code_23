#day 2 of AOC23

import fileinput

filename = 'day2_input.txt'

#Puzzle 1
sum = 0

for line in fileinput.input(files = filename):
    line_split = line.split(" ")
    for i in range(2, (len(line_split)) - 1):
        #boolean to track if a game is possible
        possible = True
        if line_split[i].isdigit():
            #check for the three cases, as soon as an impossible case occurs, break and go to the next game
            if (int(line_split[i]) > 12 and 'red' in line_split[i+1]):
                possible = False
                break
            elif (int(line_split[i]) > 13 and 'green' in line_split[i+1]):
                possible = False
                break
            elif (int(line_split[i]) > 14 and 'blue' in line_split[i+1]):
                possible = False
                break
    if possible:
        sum += int(line_split[1][:-1])

print(sum)

#Puzzle 2
sum = 0

for line in fileinput.input(files = filename):
    line_split = line.split(" ")
    #track max number of cubes for each color
    red = 0
    blue = 0
    green = 0
    for i in range(2, (len(line_split)) - 1):
        if line_split[i].isdigit():
            #adapt cases a little to check for max number of each color
            if ('red' in line_split[i+1] and int(line_split[i]) > red):
                red = int(line_split[i])
            elif ('blue' in line_split[i+1] and int(line_split[i]) > blue):
                blue = int(line_split[i])
            elif ('green' in line_split[i+1] and int(line_split[i]) > green):
                green = int(line_split[i])
    sum += red * blue * green

print(sum)
