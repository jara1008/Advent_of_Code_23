#day 3 of AOC23

import fileinput

filename = 'day3_input.txt'

#Puzzle 1
#check if the entry at an index is symbol
def sym(i, j):
    if arr[i][j].isdigit(): return True
    elif arr[i][j]=='.': return True
    else: return False

#check for an entry if it is part or not
def check_around(i, j):
    return sym(i-1, j-1) and sym(i-1, j) and sym(i-1, j+1) and sym(i, j-1) and sym(i, j+1) and sym(i+1, j-1) and sym(i+1, j) and sym(i+1, j+1)

#variable to sum up result   
sum = 0

#make a grid with lines only containing '.' on each side
arr_input = [[c for c in line] for line in fileinput.input(files = filename)]
arr = [['.' for _ in range(len(arr_input[0]) + 2)] for _ in range(len(arr_input) + 2)]
for i in range(len(arr_input) + 2):
    for j in range(len(arr_input[0]) + 1):
        if (i == 0 or j == 0 or i == len(arr_input)+1 or j == len(arr_input[0])):
            arr[i][j] = '.'
        else:
            arr[i][j] = arr_input[i-1][j-1]

#search grid for numbers
j = 1
for i in range(1, len(arr)):
    while j < len(arr[0]):
        num = ''
        boo = True
        if arr[i][j].isdigit():
            while arr[i][j].isdigit():
                num += arr[i][j]
                boo = boo and check_around(i, j)
                j += 1
            if not boo:
                sum += int(num)
        else: j += 1
    j = 1

print(sum)

#Puzzle 2
#reuse arr from above
sum = 0

#get digits at some index, if no digit there return -1
def get_digit(i, j):
    j_const = j
    if arr[i][j].isdigit():
        num = ''
        while arr[i][j].isdigit():
            num = arr[i][j] + num
            j -= 1
        j = j_const+1
        while arr[i][j].isdigit():
            num += arr[i][j]
            j += 1
        return int(num)
    return -1

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '*':
            digits = [-1, -1, -1, -1, -1, -1, -1, -1]
            if arr[i-1][j-1].isdigit(): 
                digits[0] = get_digit(i-1, j-1)
            if arr[i-1][j].isdigit():
                digits[1] = get_digit(i-1, j)
            if arr[i-1][j+1].isdigit():
                digits[2] = get_digit(i-1, j+1)
            if arr[i][j-1].isdigit(): 
                digits[3] = get_digit(i, j-1)
            if arr[i][j+1].isdigit(): 
                digits[4] = get_digit(i, j+1)
            if arr[i+1][j-1].isdigit(): 
                digits[5] = get_digit(i+1, j-1)
            if arr[i+1][j].isdigit(): 
                digits[6] = get_digit(i+1, j)
            if arr[i+1][j+1].isdigit(): 
                digits[7] = get_digit(i+1, j+1)
            intermediate_res = []
            for k in range(len(digits)):
                #if the same digit is at multiple indicies, only keep it once
                if digits[k] not in digits[k+1:] and digits[k] != -1:
                    intermediate_res.append(digits[k])
            #if there are two different digits, then comput the factor and add
            if len(intermediate_res) > 1: 
                factor = 1
                for e in intermediate_res:
                    factor *= e
                sum += factor
                
print(sum)
        

            



        





