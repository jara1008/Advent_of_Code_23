# day 23 of AOC23

import fileinput
import heapq
import sys

sys.setrecursionlimit(2000)
filename = 'day23_input.txt'

#puzzle 1
def find_paths(grid):
    queue = []
    paths = [] #remember the length of all paths
    if grid[2][1]=='.':
        heapq.heappush(queue, (2, 2, 1, {(2, 1)}))
    if grid[1][2]=='.':
        heapq.heappush(queue, (2, 1, 2, {(1, 2)}))
    while len(queue)>0:
        d, i, j, path = heapq.heappop(queue)
        if i==len(grid)-2 and j==len(grid[0])-2:
            paths.append(d+1)
            continue
        new_path = path.copy()
        new_path.add((i, j))
        if grid[i][j]=='^':
            if (i-1, j) not in path:
                heapq.heappush(queue, (d+1, i-1, j, new_path))
        elif grid[i][j]=='v':
            if (i+1, j) not in path:
                heapq.heappush(queue, (d+1, i+1, j, new_path))
        elif grid[i][j]=='<':
            if (i, j-1) not in path:
                heapq.heappush(queue, (d+1, i, j-1, new_path))
        elif grid[i][j]=='>':
            if (i, j+1) not in path:
                heapq.heappush(queue, (d+1, i, j+1, new_path))
        elif grid[i][j]=='.':
            if (i-1, j) not in path and grid[i-1][j]!='#':
                heapq.heappush(queue, (d+1, i-1, j, new_path))
            if (i+1, j) not in path and grid[i+1][j]!='#':
                heapq.heappush(queue, (d+1, i+1, j, new_path))
            if (i, j-1) not in path and grid[i][j-1]!='#':
                heapq.heappush(queue, (d+1, i, j-1, new_path))
            if (i, j+1) not in path and grid[i][j+1]!='#':
                heapq.heappush(queue, (d+1, i, j+1, new_path))
    return paths
                
grid = []
for line in fileinput.input(files = filename):
    help = []
    for e in line.strip():
        help.append(e)
    grid.append(help)

result = find_paths(grid)
result.sort()
print(result[len(result)-1])

#puzzle 2
#note: this approach is inefficient and takes roughly 2min to compute the result
def get_edges(i, j, node_index, cost, last_i, last_j):
    if i>=len(grid) or j>=len(grid[0]) or new_grid[i][j]=='#':
        if (i==21 and j==21): print(new_grid[i][j])
        return
    if (i, j) in nodes:
        index = nodes.index((i, j))
        edges[node_index][index] = cost
    else:
        if last_i!=i-1:
            get_edges(i-1, j, node_index, cost+1, i, j)
        if last_i!=i+1:
            get_edges(i+1, j, node_index, cost+1, i, j)
        if last_j!=j-1:
            get_edges(i, j-1, node_index, cost+1, i, j)
        if last_j!=j+1:
            get_edges(i, j+1, node_index, cost+1, i, j)

def find_paths_graph(i, j, paths, cost, path):
    if (i, j)==nodes[1]:
        if cost>max[0]: max[0]=cost
        return
    index = nodes.index((i, j))
    for e in range(len(edges[index])):
        tup = (nodes[e][0], nodes[e][1])
        if edges[index][e]!=-1 and tup not in path:
            path.add((i, j))
            find_paths_graph(nodes[e][0], nodes[e][1], paths, cost+edges[index][e], path)
            path.remove((i, j))
    return

new_grid = []
for line in grid:
    help = []
    for e in line:
        if e!='#':
            help.append('.')
        else:
            help.append('#')
    new_grid.append(help)

nodes = []
nodes.append((1, 1))
nodes.append((len(new_grid)-2, len(new_grid[0])-2))
for i in range(1, len(new_grid)-1, 1):
    for j in range(1, len(new_grid[0])-1, 1):
        if new_grid[i][j]=='.':
            outgoing = 0
            if new_grid[i-1][j]=='.': outgoing+=1
            if new_grid[i+1][j]=='.': outgoing+=1
            if new_grid[i][j-1]=='.': outgoing+=1
            if new_grid[i][j+1]=='.': outgoing+=1
            if outgoing >= 3:
                nodes.append((i, j))
                
edges = []
for n in nodes:
    arr = []
    for node in nodes:
        arr.append(-1)
    edges.append(arr)

for i in range(len(nodes)):
    node = nodes[i]
    get_edges(node[0]+1, node[1], i, 1, node[0], node[1])
    get_edges(node[0]-1, node[1], i, 1, node[0], node[1])
    get_edges(node[0], node[1]+1, i, 1, node[0], node[1])
    get_edges(node[0], node[1]-1, i, 1, node[0], node[1])

max = [0]
find_paths_graph(1, 1, [], 2, set())
print(max[0])