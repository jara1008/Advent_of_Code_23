# day 15 of AOC23

import fileinput

filename = 'day15_input.txt'

#puzzle 1
#for given string get value from the defined hash function
def hash(e):
    curr_str = e
    curr_val = 0
    for s in curr_str:
        curr_val += ord(s)
        curr_val *= 17
        curr_val = curr_val%256
    return curr_val

#make input array with strings separated by comma
input_strings = []
for line in fileinput.input(files = filename):
    for e in line.strip().split(','): input_strings.append(e)

#add up
total = 0
for e in input_strings:
    curr_val = hash(e)
    total += curr_val
print(total)

#puzzle 2
#track boxes and values
boxes = [[] for i in range(256)]
values = [[] for i in range(256)]

for e in input_strings:
    #track the lens/string in s and the number in num (if there is one)
    curr_str = e
    k = 0
    s = ''
    while e[k] not in '-=':
        s+=e[k]
        k+=1
    num = e[k+1:]
    #get the relevant box with the hash function
    index_box = hash(s)
    #if there is a =, we want to append/replace something
    if num!='':
        #lens does not exist, we add it
        if s not in boxes[index_box]:
            boxes[index_box].append(s)
            values[index_box].append(num)
        #lens does exist we update it's value
        else:
            index = boxes[index_box].index(s)
            values[index_box][index] = num
    #there is a -, we want to (possibly) remove a lens
    else:
        #the lens exists, we remove it
        if s in boxes[index_box]:
            index = boxes[index_box].index(s)
            boxes[index_box].pop(index)
            values[index_box].pop(index)

#add up accordingly
total = 0
for i in range(len(boxes)):
    for j in range(len(boxes[i])):
        total += (i+1) * (j+1) * int(values[i][j])
print(total)