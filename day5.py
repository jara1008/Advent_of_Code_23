#day 5 of AOC23

import fileinput

filename = 'day5_input.txt'

#puzzle 1
def update_nums(seed, input):
    boo = False
    for i in range(len(input)):
        line = input[i]
        if len(line) == 3:
            if seed >= int(line[1]) and seed < int(line[1]) + int(line[2]) and not boo:
                seed = seed - int(line[1]) + int(line[0])
                boo = True
        else:
            boo = False
    return seed

seeds = []
input = []

i = 0
for line in fileinput.input(files = filename):
    if i==0:
        for s in line.strip().split(' '):
            if s.isdigit():
                seeds.append(int(s))
    else:
        input.append(line.strip().split(' '))
    i += 1

seeds_copy = []
for i in range(len(seeds)):
    seeds_copy.append(seeds[i])

for i in range(len(seeds)):
    seeds[i] = update_nums(seeds[i], input)
seeds.sort()
print(seeds[0])

#puzzle 2
def update_ranges(seeds, arr_of_maps, index):
    boo = False
    for arr in map:
        if seeds[index] >= arr[1] and seeds[index+1] <= arr[1] + arr[2] and not boo:
            seeds[index] = seeds[index] - arr[1] + arr[0]
            seeds[index+1] = seeds[index+1] - arr[1] + arr[0]
            boo = True
        elif seeds[index] >= arr[1] and seeds[index] <= arr[1] + arr[2] and not boo:
            seeds.append(seeds[index] - arr[1] + arr[0])
            seeds.append(arr[0] + arr[2])
            seeds[index] = arr[1] + arr[2]
            seeds[index+1] = seeds[index+1]
        elif seeds[index+1] >= arr[1] and seeds[index+1] <= arr[1] + arr[2] and not boo:
            seeds.append(arr[0])
            seeds.append(seeds[index+1] - arr[1] + arr[0])
            seeds[index] = seeds[index]
            seeds[index+1] = arr[1]
            boo = True
        elif seeds[index] < arr[1] and seeds[index+1] > arr[1] + arr[2] and not boo:
            seeds.append(seeds[index])
            seeds.append(arr[1])
            seeds[index] = arr[1] + arr[2]
            seeds[index+1] = seeds[index+1]
            seeds.append(arr[0])
            seeds.append(arr[0] + arr[2])
    boo = False
    
arr_of_maps = []
maps = []
for i in range(len(input)):
    if len(input[i])==3:
        maps.append([int(e) for e in input[i]])
    else:
        arr_of_maps.append(maps)
        maps = []
arr_of_maps.append(maps)

while([] in arr_of_maps): arr_of_maps.remove([])

for map in arr_of_maps:
    map.sort(key=lambda x: x[1])

seeds_ranges = []
for i in range(0, len(seeds_copy), 2):
    seeds_ranges.append(seeds_copy[i])
    seeds_ranges.append(seeds_copy[i] + seeds_copy[i+1] -1)

for map in arr_of_maps:
    length = len(seeds_ranges)
    for i in range(0, length, 2):
        update_ranges(seeds_ranges, map, i)

print(min(seeds_ranges))


    


    






