#day 4 of AOC23

import fileinput

filename = 'day4_input.txt'

#Puzzle 1
sum = 0
for line in fileinput.input(files = filename):
    winning_nums = []
    my_nums = []
    #make arrays for different types of numbers: winning_nums | my_nums
    for c in line.rstrip('\n').split(' '):
        #Attention 10 hardcoded! Would need to be changed according to input!
        if c.isdigit() and len(winning_nums)<10:
            winning_nums.append(int(c))
        elif c.isdigit(): 
            my_nums.append(int(c))
    #sum up same digits with specified weight
    sum_per_round = 0
    for n in my_nums:
        if n in winning_nums and sum_per_round==0:
            sum_per_round = 1
        elif n in winning_nums:
            sum_per_round *= 2
    sum += sum_per_round

print(sum)

#Puzzle 2
#keep array with total number of each card
cards = [1 for line in (fileinput.input(files = filename))]

card_no = 0
for line in fileinput.input(files = filename):
    winning_nums = []
    my_nums = []
    for c in line.rstrip('\n').split(' '):
        if c.isdigit() and len(winning_nums)<10:
            winning_nums.append(int(c))
        elif c.isdigit(): 
            my_nums.append(int(c))
    #only from here code is changed, upper code is redundant...
    curr_card_num = card_no+1
    for n in my_nums:
        if n in winning_nums:
            cards[curr_card_num] += cards[card_no]
            curr_card_num += 1
    card_no += 1

sum = 0
for e in cards:
    sum += e
print(sum)