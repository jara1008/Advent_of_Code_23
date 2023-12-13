# day 13 of AOC23

import fileinput

filename = 'day13_input.txt'

#puzzle 1
#make 3D array with the inputs
inputs = []
cur_input = []
for line in fileinput.input(files = filename):
    cur_line = []
    if line=='\n':
        inputs.append(cur_input) 
        cur_input = []
    else:
        for e in line.strip():
            cur_line.append(e)
        cur_input.append(cur_line)
inputs.append(cur_input)

#remember index of middle of reflection
index_at = [-1 for i in range(len(inputs))]
#remember whether symmetrie is horizontal or vertical
row_or_col = [-1 for i in range(len(inputs))] #0==row, 1==col

#get all horizontal reflections
for inp in range(len(inputs)):
    cur = inputs[inp]
    for i in range(len(cur)-1):
        #if two lines are equal check symmetries from there on
        if cur[i]==cur[i+1]:
            index = 1
            while i-index >= 0 and i+1+index<len(cur) and cur[i-index]==cur[i+1+index]:
                index += 1
            #if symmetry is accross entire field track it in arrays
            if i-index == -1 or i+1+index==len(cur):
                index_at[inp]=i
                row_or_col[inp]=0

#get all vertical reflections
for inp in range(len(inputs)):
    cur = inputs[inp]
    for i in range(len(cur[0])-1):
        #use boolean to check if two columns are equal
        boo = True
        for j in range(len(cur)):
            if cur[j][i]!=cur[j][i+1]: 
                #colums are not equal, set boo to true and break loop
                boo = False
            if not boo: break
        #two equal columns are found -> check symmetries from there on
        if boo:
            index = 1
            #tracks if columns are equal
            boo_snd = True
            while boo_snd and i-index >= 0 and i+1+index<len(cur[0]):
                for m in range(len(cur)):
                    if cur[m][i-index]!=cur[m][i+1+index]: 
                        boo_snd = False
                #columns are still equal, increase index
                if boo_snd and i-index >= 0 and i+1+index<len(cur[0]):
                    index += 1
            #symmetry accross entire field, track it
            if i-index == -1 or i+1+index==len(cur[0]):
                index_at[inp]=i
                row_or_col[inp]=1

#sum up accordingly
total = 0
for i in range(len(index_at)):
    if row_or_col[i]==0:
        total += (index_at[i]+1)*100
    else:
        total += (index_at[i]+1)

print(total)

#puzzle 2
#remember indicies where reflections start and if reflection is horizontal or vertical
index_at = [-1 for i in range(len(inputs))]
row_or_col = [-1 for i in range(len(inputs))] #0==row, 1==col

#get horizontal reflections -> go through element by element, if one does not match error+=1
for inp in range(len(inputs)):
    cur = inputs[inp]
    for i in range(len(cur)-1):
        error = 0
        for j in range(len(cur[0])):
            if cur[i][j]!=cur[i+1][j]: error+=1
        #if error in a line is small enough, check for further symmetries
        if error<=1:
            index = 1
            while i-index >= 0 and i+1+index<len(cur):
                for k in range(len(cur[0])):
                    #count errors
                    if cur[i-index][k]!=cur[i+1+index][k]: error+=1
                index+=1
            #check if exactly one error occurs and if reflection is accross entire field
            if error==1 and (i-index == -1 or i+1+index==len(cur)):
                index_at[inp]=i
                row_or_col[inp]=0

#do the same for horizontal symmetries
for inp in range(len(inputs)):
    cur = inputs[inp]
    for i in range(len(cur[0])-1):
        error = 0
        for j in range(len(cur)):
            if cur[j][i]!=cur[j][i+1]: error+=1
        #if error in a line is small enough, check for further symmetries
        if error<=1:
            index = 1
            while error<=1 and i-index >= 0 and i+1+index<len(cur[0]):
                for m in range(len(cur)):
                    if cur[m][i-index]!=cur[m][i+1+index]: error+=1
                if error<=1 and i-index >= 0 and i+1+index<len(cur[0]):
                    index += 1
            #check if exactly one error occurs and if reflection is accross entire field
            if error==1 and (i-index == -1 or i+1+index==len(cur[0])):
                index_at[inp]=i
                row_or_col[inp]=1

#sum up accordingly
total = 0
for i in range(len(index_at)):
    if row_or_col[i]==0:
        total += (index_at[i]+1)*100
    else:
        total += (index_at[i]+1)

print(total)