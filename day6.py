# day 6 of AOC23

import fileinput

filename = 'day6_input.txt'

#puzzle 1
#finds the number of possible ways for a given time and distance
def find_options(time, distance):
    add = 0
    curr_time = time-1
    #we beginn for time-1 and go until the current pressing time would yield a better distance
    while (time - curr_time)*curr_time <= distance:
        curr_time -= 1
    #we go lower the current pressing time until it does no longer yield a better distance, we add the no. of iterations
    while (time-curr_time)*curr_time > distance:
        add += 1
        curr_time -= 1
    return add


times = []
distances = []
line_nr = 0
for line in fileinput.input(files = filename):
    if line_nr == 0:
        for e in line.strip().split(" "):
            if e.isdigit():
                times.append(int(e))
        line_nr = 1
    else:
        for e in line.strip().split(" "):
            if e.isdigit():
                distances.append(int(e))

#compute the number of ways for given (time, distance), directly multiply them together
res = 1
for i in range(len(times)):
    res *= find_options(times[i], distances[i])

print(res)

#puzzle 2
#note: this solution takes a few seconds for my input (~5sec.), it might not be the most efficient approach 
time = ''
distance = ''

#build the needed numbers from our previous arrays, usees int to str cast to do so
for i in range(len(times)):
    time += str(times[i])
    distance += str(distances[i])

print(find_options(int(time), int(distance)))
