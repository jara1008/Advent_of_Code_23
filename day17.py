# day 17 of AOC23

import fileinput
import heapq

filename = 'day17_input.txt'

#puzzle 1
#run dijkstra to find shortest paths
def dijkstra(tiles):
    #track visited nodes
    visited = set()
    #reachable nodes from already visited nodes
    to_visit = [(0, 0, 0, 'r', 1), (0, 0, 0, 'd', 1)] #value, i, i, dir, count
    while len(to_visit) > 0:
        #take reachable node with smallest cost to get there
        curr = heapq.heappop(to_visit)
        #when already been there -> continue, shortest path is already known
        if (curr[1], curr[2], curr[3], curr[4]) in visited: continue
        else: visited.add((curr[1], curr[2], curr[3], curr[4]))
        #get new indicies depending on direction
        if curr[3]=='d': 
            new_i = curr[1]+1 
            new_j = curr[2]
        if curr[3]=='u': 
            new_i = curr[1]-1 
            new_j = curr[2]
        if curr[3]=='l': 
            new_i = curr[1]
            new_j = curr[2]-1
        if curr[3]=='r': 
            new_i = curr[1] 
            new_j = curr[2]+1
        #out of bounds -> continue
        if new_i < 0 or new_j < 0 or new_i >= len(tiles) or new_j >= len(tiles[0]): continue
        #compute cost for new indicies 
        new_val = curr[0]+tiles[new_i][new_j]
        #check if not more than 3 tiles in a row in the same directions were crossed
        if curr[4] <= 3:
            #if at final point return value
            if new_i == len(tiles) - 1 and new_j == len(tiles[0]) - 1:
                return new_val
        #check for reachable nodes that are allowed under the constraints
        for d in 'lrdu':
            if (curr[3]=='r' and d=='l') or (curr[3]=='l' and d=='r'): continue
            if (curr[3]=='d' and d=='u') or (curr[3]=='u' and d=='d'): continue
            if d==curr[3] and curr[4]+1 > 3: continue
            elif d==curr[3]:
                heapq.heappush(to_visit, (new_val, new_i, new_j, d, curr[4]+1))
            else:
                heapq.heappush(to_visit, (new_val, new_i, new_j, d, 1))

#input               
tiles = []

for line in fileinput.input(files = filename):
    help = []
    for e in line.strip():
        help.append(int(e))
    tiles.append(help)

print(dijkstra(tiles))

#puzzle 2
#same a above but a little adjusted
def dijkstra_with_lengths(tiles, min_length, max_length):
    visited = set()
    to_visit = [(0, 0, 0, 'r', 1), (0, 0, 0, 'd', 1)] #value, i, i, dir, count
    while len(to_visit) > 0:
        curr = heapq.heappop(to_visit)
        if (curr[1], curr[2], curr[3], curr[4]) in visited: continue
        else: visited.add((curr[1], curr[2], curr[3], curr[4]))
        if curr[3]=='d': 
            new_i = curr[1]+1 
            new_j = curr[2]
        if curr[3]=='u': 
            new_i = curr[1]-1 
            new_j = curr[2]
        if curr[3]=='l': 
            new_i = curr[1]
            new_j = curr[2]-1
        if curr[3]=='r': 
            new_i = curr[1] 
            new_j = curr[2]+1
        if new_i < 0 or new_j < 0 or new_i >= len(tiles) or new_j >= len(tiles[0]): continue
        new_val = curr[0]+tiles[new_i][new_j]
        #instead of only checking maxiumum length also check minimum length
        if curr[4] >= min_length and curr[4] <= max_length:
            if new_i == len(tiles) - 1 and new_j == len(tiles[0]) - 1:
                return new_val
        for d in 'lrdu':
            if (curr[3]=='r' and d=='l') or (curr[3]=='l' and d=='r'): continue
            if (curr[3]=='d' and d=='u') or (curr[3]=='u' and d=='d'): continue
            if d==curr[3] and curr[4]+1 > max_length: continue
            #when we change directions check wheter at least 4 (=min_length) tiles were crossed in prev. direction
            if d!=curr[3] and curr[4] < min_length: continue
            elif d==curr[3]:
                heapq.heappush(to_visit, (new_val, new_i, new_j, d, curr[4]+1))
            else:
                heapq.heappush(to_visit, (new_val, new_i, new_j, d, 1))

print(dijkstra_with_lengths(tiles, 4, 10))