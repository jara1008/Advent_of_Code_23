# day 20 of AOC23

import fileinput

filename = 'day20_input.txt'

#puzzle 1
#simulates pressing the button once, counting high and low pulses
def press_button(low, high):
    #queue used to keep order of pulses
    queue = []
    #low pulse from all broadcaster outputs are sent out
    for i in broadcast:
        queue.append(i)
        low += 1
    while len(queue) > 0:
        origin, name, freq = queue.pop(0)
        #if current module is flipflop and pulse received is low, go into this case
        if name in flip_flops_keys_only and freq==0:
            index = flip_flops_keys_only.index(name)
            if flip_flops_keys[index][1]=='off':
                flip_flops_keys[index] = (name, 'on')
                for dest in flip_flops_val[index]:
                    queue.append((name, dest, 1))
                    high += 1
            else:
                flip_flops_keys[index] = (name, 'off')
                for dest in flip_flops_val[index]:
                    queue.append((name, dest, 0))
                    low += 1
        #if current module is conjunction go into this case
        elif name in conj_keys_only:
            index = conj_keys_only.index(name)
            #set the pulse received from the sender for this conjunction module to high/low
            for k in range(len(conj_get_val[index][1])):
                if conj_get_val[index][1][k][0]==origin:
                    conj_get_val[index][1][k] = (origin, freq)
            boo = False
            #count if all remembered pulses for this conjunction are high -> boo stays false
            for k in range(len(conj_get_val[index][1])):
                if conj_get_val[index][1][k][1]==0:
                    boo=True
            #not all remembered pulses are high -> send out high pulse
            if boo:
                for dest in conj_val[index]:
                    queue.append((name, dest, 1))
                    high += 1
            #all remembered pulses are high -> send out low pulse
            else:
                for dest in conj_val[index]:
                    queue.append((name, dest, 0))
                    low += 1
    return [low, high]

#initializes the input
def initialize():
    for line in fileinput.input(files = filename):
        arr = line.strip().split("->")
        if arr[0][0] == '%':
            flip_flops_keys_only.append(arr[0][1:].strip())
            flip_flops_keys.append((arr[0][1:].strip(), 'off'))
            flip_flops_val.append(arr[1].strip().split(', '))
        elif arr[0][0] == '&':
            conj_keys_only.append(arr[0][1:].strip())
            conj_get_val.append((arr[0][1:].strip(), []))
            conj_val.append(arr[1].strip().split(', '))
        else:
            for i in arr[1].strip().split(', '):
                broadcast.append((-1, i, 0))

    for flip in flip_flops_keys_only:
        index = flip_flops_keys_only.index(flip)
        dests = flip_flops_val[index]
        for dest in dests:
            if dest in conj_keys_only:
                index_dest = conj_keys_only.index(dest)
                name, tups = conj_get_val[index_dest]
                tups.append((flip, 0))
                conj_get_val[index_dest] = (name, tups)

    for flip in conj_keys_only:
        index = conj_keys_only.index(flip)
        dests = conj_val[index]
        for dest in dests:
            if dest in conj_keys_only:
                index_dest = conj_keys_only.index(dest)
                name, tups = conj_get_val[index_dest]
                tups.append((flip, 0))
                conj_get_val[index_dest] = (name, tups)

#arrays to store the input, used in initialize
flip_flops_val = []
flip_flops_keys = []
flip_flops_keys_only = []
conj_val = []
conj_keys_only = []
conj_get_val = []
broadcast = []
initialize()

#press button 1000x -> call function press_button 1000x and adjust the values low/high accordingly
low = 0
high = 0
for i in range(1000):
    res = press_button(low, high)
    #plus one for pushing the button itself
    low = res[0]+1
    high = res[1]
print(low*high)

#puzzle 2
#similar function as above: instead of counting pulses, it returns True if and only if the conjunction n sends out a high pulse
def press_button_no_count(n):
    queue = []
    for i in broadcast:
        queue.append(i)
    while len(queue) > 0:
        origin, name, freq = queue.pop(0)
        if name in flip_flops_keys_only and freq==0:
            index = flip_flops_keys_only.index(name)
            if flip_flops_keys[index][1]=='off':
                flip_flops_keys[index] = (name, 'on')
                for dest in flip_flops_val[index]:
                    queue.append((name, dest, 1))
            else:
                flip_flops_keys[index] = (name, 'off')
                for dest in flip_flops_val[index]:
                    queue.append((name, dest, 0))
        elif name in conj_keys_only:
            index = conj_keys_only.index(name)
            for k in range(len(conj_get_val[index][1])):
                if conj_get_val[index][1][k][0]==origin:
                    conj_get_val[index][1][k] = (origin, freq)
            boo = False
            for k in range(len(conj_get_val[index][1])):
                if conj_get_val[index][1][k][1]==0:
                    boo=True
            if boo:
                for dest in conj_val[index]:
                    queue.append((name, dest, 1))
                #sends out true if n sends out a high pulse
                if name==n: return True
            else:
                for dest in conj_val[index]:
                    queue.append((name, dest, 0))
    return False

#all conjunctions that send out to 'kl' -> 'rx'
conj_to_send_high = []
for i in range(len(conj_keys_only)):
    if 'kl' in conj_val[i]: conj_to_send_high.append(conj_keys_only[i])

total = 1  
for n in conj_to_send_high:
    #initialize to start position
    flip_flops_val = []
    flip_flops_keys = []
    flip_flops_keys_only = []
    conj_val = []
    conj_keys_only = []
    conj_get_val = []
    broadcast = []
    initialize()
    #count how many button presses for each conjunction in conj_to_send_high
    count = 1
    while not press_button_no_count(n): count+=1
    total*=count
print(total)