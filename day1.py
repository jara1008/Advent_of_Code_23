#day 1 of AOC23

import fileinput

filename = 'day1_input.txt'

#Puzzle 1
sum = 0

for line in fileinput.input(files = filename):
    fst = ''
    snd = ''
    for c in line:
        if c.isdigit():
            fst = c
            break
    
    for c in reversed(line):
        if c.isdigit():
            snd = c
            break
    num = str(fst) + str(snd)
    sum += int(num)

print(sum)

#Puzzle 2
sum = 0
numbers = {'one': '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

for line in fileinput.input(files = filename):
    br = False
    br2 = False
    fst = ''
    snd = ''
    for i in range(len(line)):
        if line[i].isdigit():
            fst = line[i]
            break
        for key in numbers:
            if line.startswith(key, i):
                fst = numbers[key]
                br = True
                break
        if br:
            break

    for i in range(len(line)):
        if line[len(line)-i-1].isdigit():
            snd = line[len(line)-i-1]
            break
        for key in numbers:
            if line.startswith(key, len(line)-i-1):
                snd = numbers[key]
                br2 = True
                break
        if br2:
            break
    
    num = str(fst) + str(snd)
    sum += int(num)
    
print(sum)