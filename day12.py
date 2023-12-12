# day 12 of AOC23

import fileinput
import functools

filename = 'day12_input.txt'   

#puzzle 1
#using recursion produce every possible sequence and check whether it is valid
def rec(s, nums, index):
    if index==len(s):
        arr=[]
        boo = False
        curr = 0
        for i in range(len(s)):
            if s[i]=='#' and boo: 
                curr+=1
            elif s[i]=='#':
                curr=1
                boo=True
            elif s[i]!='#' and boo:
                if curr!= 0: 
                    arr.append(curr)
                    curr=0
                boo=False
        if curr!= 0: 
            arr.append(curr)
        if arr==nums:
            return 1
        else: return 0
    else:
        if s[index]=='?':
            s[index]='.'
            add=rec(s, nums, index+1)
            s[index]='#'
            add+=rec(s, nums, index+1)
            s[index]='?'
            return add
        else: 
            return rec(s, nums, index+1)
        
seq = []
missing = []
for line in fileinput.input(files = filename):
    arr = []
    line = line.split()
    for e in line[1].split(','):
        arr.append(int(e))
    seq.append([e for e in line[0]])
    missing.append(arr)

count = 0
for i in range(len(seq)):
    count+=rec(seq[i], missing[i], 0)
print(count)

#puzzle 2
@functools.cache
def cached_rec(s, nums, index, curr, damaged):
    #Base Case: we used our entire string
    if len(s)==0:
        #the last elements was a #
        if damaged:
            #the number of # does not align with the wanted number
            if nums[index]!=curr:
                return 0
            index+=1
        #if this fails then we do not have all numbers covered
        if index!=len(nums):
            return 0
        return 1
    #we already have all numbers covered, if there are more # then the sequence is not valid
    if index >= len(nums) and s[0]=='#': return 0
    #we have to substitue the ? with all posibilites
    elif s[0]=='?':
        #Note: we make a new string
        new_s = '#'+s[1:]
        add = cached_rec(new_s, nums, index, curr, damaged)
        new_s = '.'+s[1:]
        add += cached_rec(new_s, nums, index, curr, damaged)
        return add
    #we found the first # of a sequence -> damaged=True and curr=1
    elif s[0]=='#' and not damaged:
        return cached_rec(s[1:], nums, index, 1, True)
    #we are in a sequence of #
    elif s[0]=='#':
        #if the sequence of # is longer than the current number, the sequence is not valid
        if nums[index]<curr:
            return 0
        #else we continue by counting the #
        return cached_rec(s[1:], nums, index, curr+1, damaged)
    #we encountered a . -> our sequence of # is terminated and needs to be compared to the current number
    elif damaged:
        #there not the same -> invalid sequence
        if curr!=nums[index]:
            return 0
        #they are the same -> continue with the next number, current is again 0
        return cached_rec(s[1:], nums, index+1, 0, False)
    #simply a . and no sequence of # stopped, take away . and continue
    return cached_rec(s[1:], nums, index, curr, damaged)

#adapt input, use strings and tuples, else we cannot use automatic memoization
seq_str = []
missing_tup = []
for i in range(len(seq)):
    word=''
    for e in seq[i]:
        word+=e
    word+='?'
    seq_str.append((word*5)[:-1])
    missing_tup.append(tuple(missing[i]*5))

count=0
for i in range(len(seq)):
    count+=cached_rec(seq_str[i], missing_tup[i], 0, 0, False)

print(count)