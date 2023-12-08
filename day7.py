# day 7 of AOC23

import fileinput

filename = 'day7_input.txt'

#puzzle 1
def get_ranks(cardInput):
    five = []
    four = []
    full = []
    three = []
    tpair = []
    pair = []
    highC = []
    for c in cardInput:
        cards = c[0].copy()
        cards_copy = c[0].copy()
        cards.sort()
        if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]: five.append([cards_copy,c[1]])
        elif cards[0] == cards[1] == cards[2] == cards[3] or cards[4] == cards[1] == cards[2] == cards[3]: four.append([cards_copy,c[1]])
        elif cards[0] == cards[1] and cards[2] == cards[3] == cards[4] or cards[0] == cards[1] == cards[2] and cards[3] == cards[4]: full.append([cards_copy,c[1]])
        elif cards[0] == cards[1] == cards[2] or cards[3] == cards[1] == cards[2] or cards[4] == cards[3] == cards[2]: three.append([cards_copy,c[1]])
        elif cards[0] != cards[1] != cards[2] != cards[3] != cards[4]: highC.append([cards_copy,c[1]])
        elif cards[0] == cards[1] and cards[2] != cards[3] != cards[4] or cards[1] == cards[2] and cards[0] != cards[3] != cards[4] or cards[3] == cards[2] and cards[0] != cards[1] != cards[4] or cards[3] == cards[4] and cards[0] != cards[1] != cards[2]: pair.append([cards_copy,c[1]])
        else: tpair.append([cards_copy,c[1]])
    five.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    four.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    full.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    three.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    tpair.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    pair.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    highC.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))

    total = 0
    i=1
    for j in highC:
        total += i*int(j[1])
        i+=1
    for j in pair:
        total += i*int(j[1])
        i+=1
    for j in tpair:
        total += i*int(j[1])
        i+=1
    for j in three:
        total += i*int(j[1])
        i+=1
    for j in full:
        total += i*int(j[1])
        i+=1
    for j in four:
        total += i*int(j[1])
        i+=1
    for j in five:
        total += i*int(j[1])
        i+=1
    return (total)


cardInput = []

index = 0
for line in fileinput.input(files = filename):
    split = line.strip().split(' ')
    cardInput.append(split)
    arr = split[0]
    arr_int = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        if arr[i] == 'A': arr_int[i] = 9
        elif arr[i] == 'K': arr_int[i] = 8
        elif arr[i] == 'Q': arr_int[i] = 7
        elif arr[i] == 'J': arr_int[i] = 6
        elif arr[i] == 'T': arr_int[i] = 5
        else: arr_int[i] = int(arr[i])-5
    cardInput[index][0] = arr_int
    arr_int = [0 for i in range(len(arr))]    
    index += 1

print(get_ranks(cardInput))

#puzzle 2
def get_ranks_joker(cardInput):
    five = []
    four = []
    full = []
    three = []
    tpair = []
    pair = []
    highC = []
    for c in cardInput:
        x = 0
        max_x = 0
        cards_copy = c[0].copy()
        for j in [9, 8, 7, 5, 4, 3, 2, 1, 0, -1, -2, -3]:
            cards = c[0].copy()
            for i in range(len(cards)):
                if cards[i] == 6:
                    cards[i] = j
            cards.sort()
            if cards[0] == cards[1] == cards[2] == cards[3] == cards[4]: x=7
            elif cards[0] == cards[1] == cards[2] == cards[3] or cards[4] == cards[1] == cards[2] == cards[3]: x=6
            elif cards[0] == cards[1] and cards[2] == cards[3] == cards[4] or cards[0] == cards[1] == cards[2] and cards[3] == cards[4]: x=5
            elif cards[0] == cards[1] == cards[2] or cards[3] == cards[1] == cards[2] or cards[4] == cards[3] == cards[2]: x=4
            elif cards[0] != cards[1] != cards[2] != cards[3] != cards[4]: x=1
            elif cards[0] == cards[1] and cards[2] != cards[3] != cards[4] or cards[1] == cards[2] and cards[0] != cards[3] != cards[4] or cards[3] == cards[2] and cards[0] != cards[1] != cards[4] or cards[3] == cards[4] and cards[0] != cards[1] != cards[2]: x=2
            else: x=3
            max_x = max(x, max_x)
        for i in range(len(cards_copy)):
                if cards_copy[i] == 6:
                    cards_copy[i] = -4
        if max_x==7: five.append([cards_copy, c[1]])
        if max_x==6: four.append([cards_copy, c[1]])
        if max_x==5: full.append([cards_copy, c[1]])
        if max_x==4: three.append([cards_copy, c[1]])
        if max_x==3: tpair.append([cards_copy, c[1]])
        if max_x==2: pair.append([cards_copy, c[1]])
        if max_x==1: highC.append([cards_copy, c[1]])
    
    five.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    four.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    full.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    three.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    tpair.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    pair.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))
    highC.sort(key = lambda x: (x[0][0],x[0][1],x[0][2],x[0][3],x[0][4]))

    total = 0
    i=1
    for j in highC:
        total += i*int(j[1])
        i+=1
    for j in pair:
        total += i*int(j[1])
        i+=1
    for j in tpair:
        total += i*int(j[1])
        i+=1
    for j in three:
        total += i*int(j[1])
        i+=1
    for j in full:
        total += i*int(j[1])
        i+=1
    for j in four:
        total += i*int(j[1])
        i+=1
    for j in five:
        total += i*int(j[1])
        i+=1
    return (total)

print(get_ranks_joker(cardInput))

#246098006 to low
#247001209 to high

