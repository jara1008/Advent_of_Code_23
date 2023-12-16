# day 16 of AOC23

import fileinput
import sys

sys.setrecursionlimit(300)
filename = 'day16_input.txt'

#puzzle 1
#goes through the grid from an initial point i,j
def walk_through(i, j, dir):
    #if already been at that point with same direction return
    if track[i][j] and dir in track_dir[i][j]: 
        return
    #else track location and direction
    track[i][j]=True
    track_dir[i][j]+=dir
    if dir=='r':
        while j<len(grid[0])-1 and grid[i][j] in '-.':
            j+=1
            track[i][j]=True
            track_dir[i][j]+=dir
        if j<len(grid[0])-1 and grid[i][j]=='\\':
            walk_through(i+1, j, 'd')
        elif j<len(grid[0])-1 and grid[i][j]=='/':
            walk_through(i-1, j, 'u')
        elif j<len(grid[0])-1 and grid[i][j]=='|':
            walk_through(i-1, j, 'u')
            walk_through(i+1, j, 'd')
    if dir=='d':
        while i<len(grid)-1 and grid[i][j] in '|.':
            i+=1
            track[i][j]=True
            track_dir[i][j]+=dir
        if i<len(grid)-1 and grid[i][j]=='\\':
            walk_through(i, j+1, 'r')
        elif i<len(grid)-1 and grid[i][j]=='/':
            walk_through(i, j-1, 'l')
        elif i<len(grid)-1 and grid[i][j]=='-':
            walk_through(i, j+1, 'r')
            walk_through(i, j-1, 'l')
    if dir=='u':
        while i>0 and grid[i][j] in '|.':
            i-=1
            track[i][j]=True
            track_dir[i][j]+=dir
        if i>0 and grid[i][j]=='\\':
            walk_through(i, j-1, 'l')
        elif i>0 and grid[i][j]=='/':
            walk_through(i, j+1, 'r')
        elif i>0 and grid[i][j]=='-':
            walk_through(i, j+1, 'r')
            walk_through(i, j-1, 'l')
    if dir=='l':
        while j>0 and grid[i][j] in '-.':
            j-=1
            track[i][j]=True
            track_dir[i][j]+=dir
        if j>0 and grid[i][j]=='\\':
            walk_through(i-1, j, 'u')
        elif j>0 and grid[i][j]=='/':
            walk_through(i+1, j, 'd')
        elif j>0 and grid[i][j]=='|':
            walk_through(i-1, j, 'u')
            walk_through(i+1, j, 'd')

def null_track(track):
    for i in range(len(track)):
        for j in range(len(track[0])):
            track[i][j]=False
    return track

def null_track_dir(track_dir):
    for i in range(len(track_dir)):
        for j in range(len(track_dir[0])):
            track_dir[i][j]=''
    return track_dir

grid = []

#read input with added borders of .
for line in fileinput.input(files = filename):
    help = []
    help.append('.')
    for e in line.strip():
        help.append(e)
    help.append('.')
    grid.append(help)
grid.append(['.' for i in range(len(grid[0]))])
grid.insert(0, ['.' for i in range(len(grid[0]))])

#array to track if already been at some location
track = []
for i in range(len(grid)):
    help = []
    for e in range(len(grid[0])):
        help.append(False)
    track.append(help)

#array to track directions at specific locations
track_dir = []
for i in range(len(grid)):
    help = []
    for e in range(len(grid[0])):
        help.append('')
    track_dir.append(help)

walk_through(1, 1, 'r')
add = 0
for k in range(1, len(track)-1, 1):
    for m in range(1, len(track[k])-1, 1):
        if track[k][m]: add+=1
print(add)

#puzzle 2
maximum = 0

#top row
for n in range(1, len(track[0])-1, 1):
    track = null_track(track)
    track_dir = null_track_dir(track_dir)
    walk_through(1, n, 'd')
    add = 0
    for k in range(1, len(track)-1, 1):
        for m in range(1, len(track[k])-1, 1):
            if track[k][m]: add+=1
    if add>maximum: maximum=add

#left column
for n in range(1, len(track)-1, 1):
    track = null_track(track)
    track_dir = null_track_dir(track_dir)
    walk_through(n, 1, 'r')
    add = 0
    for k in range(1, len(track)-1, 1):
        for m in range(1, len(track[k])-1, 1):
            if track[k][m]: add+=1
    if add>maximum: maximum=add

#right column
for n in range(1, len(track)-1, 1):
    track = null_track(track)
    track_dir = null_track_dir(track_dir)
    walk_through(n, len(track[0])-1, 'l')
    add = 0
    for k in range(1, len(track)-1, 1):
        for m in range(1, len(track[k])-1, 1):
            if track[k][m]: add+=1
    if add>maximum: maximum=add

#bottom row
for n in range(1, len(track[0])-1, 1):
    track = null_track(track)
    track_dir = null_track_dir(track_dir)
    walk_through(len(track)-1, n, 'u')
    add = 0
    for k in range(1, len(track)-1, 1):
        for m in range(1, len(track[k])-1, 1):
            if track[k][m]: add+=1
    if add>maximum: maximum=add

print(maximum)