# day 19 of AOC23

import fileinput
import re

filename = 'day19_input.txt'

#puzzle 1
def check_rule(part_no, rule_no):
    letters = r_letter[rule_no]
    signs = r_signs[rule_no]
    nums = r_nums[rule_no]
    dest = r_dest[rule_no]
    index = 0
    for p in letters:
        if p=='x':
            if signs[index]=='<':
                if p_nums[part_no][0]<nums[index]:
                    return dest[index]
            elif signs[index]=='>':
                if p_nums[part_no][0]>nums[index]:
                    return dest[index]
            elif signs[index]=='.': return dest[index]
            index+=1
        elif p=='m':
            if signs[index]=='<':
                if p_nums[part_no][1]<nums[index]:
                    return dest[index]
            elif signs[index]=='>':
                if p_nums[part_no][1]>nums[index]:
                    return dest[index]
            elif signs[index]=='.': return dest[index]
            index+=1
        elif p=='a':
            if signs[index]=='<':
                if p_nums[part_no][2]<nums[index]:
                    return dest[index]
            elif signs[index]=='>':
                if p_nums[part_no][2]>nums[index]:
                    return dest[index]
            elif signs[index]=='.': return dest[index]
            index+=1
        elif p=='s':
            if signs[index]=='<':
                if p_nums[part_no][3]<nums[index]:
                    return dest[index]
            elif signs[index]=='>':
                if p_nums[part_no][3]>nums[index]:
                    return dest[index]
            elif signs[index]=='.': return dest[index]
            index+=1
        elif letters[index] not in 'xmas': return dest[index]

rules = []
parts = []
sp = True
for line in fileinput.input(files = filename):
    if line=='\n': sp=False
    elif sp:
        rules.append(re.split('[{},]', line.strip()))
    elif not sp:
        parts.append(re.split('[{},]', line.strip()))

r_names = []
r_letter = []
r_signs = []
r_nums = []
r_dest = []

for rule in rules:
    r_names.append(rule[0])
    r_letter_cur = []
    r_signs_cur = []
    r_nums_cur = []
    r_dest_cur = []
    for e in rule[1:]:
        if e=='': continue
        if e[0] not in 'AR': r_letter_cur.append(e[0])
        else: 
            r_letter_cur.append(e[0])
            r_signs_cur.append('.')
            r_nums_cur.append(-1)
            r_dest_cur.append(e[0])
            break
        rest = e.split(':')
        if len(rest)==2:
            r_signs_cur.append(e[1:2])
            r_nums_cur.append(int(rest[0][2:]))
            r_dest_cur.append(rest[1])
        else:
            r_signs_cur.append('.')
            r_nums_cur.append(-1)
            r_dest_cur.append(rest[0])
    r_letter.append(r_letter_cur)
    r_signs.append(r_signs_cur)
    r_nums.append(r_nums_cur)
    r_dest.append(r_dest_cur)

p_letter = []
p_nums = [] 

for part in parts:
    p_letter_cur = []
    p_nums_cur = []
    for p in part:
        if p=='': continue
        rest = p.split('=')
        p_letter_cur.append(rest[0])
        p_nums_cur.append(int(rest[1]))
    p_letter.append(p_letter_cur)
    p_nums.append(p_nums_cur)

total = 0
for i in range(len(p_letter)):
    cur_name = 'in'
    ret = '.'
    while ret not in 'AR':
        index = r_names.index(cur_name)
        ret = check_rule(i, index)
        cur_name = ret
    if ret=='A': total+=p_nums[i][0]+p_nums[i][1]+p_nums[i][2]+p_nums[i][3]

print(total) 

#puzzle 2
intervals = [(1, 4000, 1, 4000, 1, 4000, 1, 4000, 'in')]
total = 0

def check_rule_interval(interval):
    i = interval
    if interval[-1] in "AR":
        intervals.remove(interval)
        if interval[-1] == "A": return (i[1]+1-i[0])*(i[3]+1-i[2])*(i[5]+1-i[4])*(i[7]+1-i[6])
        return 0
    rule_no = r_names.index(interval[-1])
    letters = r_letter[rule_no]
    signs = r_signs[rule_no]
    nums = r_nums[rule_no]
    dest = r_dest[rule_no]
    for index, p in enumerate(letters):
        if p=='x':
            if signs[index]=='<':
                if interval[0] < nums[index] < interval[1]:
                    intervals.remove(interval)
                    intervals.append((nums[index],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
                    intervals.append((i[0],nums[index]-1,i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
                    break
            elif signs[index]=='>':
                if interval[0] < nums[index] < interval[1]:
                    intervals.remove(interval)
                    intervals.append((nums[index]+1,i[1],i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
                    intervals.append((i[0],nums[index],i[2],i[3],i[4],i[5],i[6],i[7],i[8]))
                    break
            elif signs[index]=='.':
                intervals.remove(interval)
                intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
                break

        elif p=='m':
            if signs[index]=='<':
                if interval[2] < nums[index] < interval[3]:
                        intervals.remove(interval)
                        intervals.append((i[0],i[1],nums[index],i[3],i[4],i[5],i[6],i[7],i[8]))
                        intervals.append((i[0],i[1],i[2],nums[index]-1,i[4],i[5],i[6],i[7],dest[index]))
                        break
            elif signs[index]=='>':
                if interval[2] < nums[index] < interval[3]:
                    intervals.remove(interval)
                    intervals.append((i[0],i[1],nums[index]+1,i[3],i[4],i[5],i[6],i[7],dest[index]))
                    intervals.append((i[0],i[1],i[2],nums[index],i[4],i[5],i[6],i[7],i[8]))
                    break
            elif signs[index]=='.':
                intervals.remove(interval)
                intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
                break

        elif p=='a':
            if signs[index]=='<':
                if interval[4] < nums[index] < interval[5]:
                    intervals.remove(interval)
                    intervals.append((i[0],i[1],i[2],i[3],nums[index],i[5],i[6],i[7],i[8]))
                    intervals.append((i[0],i[1],i[2],i[3],i[4],nums[index]-1,i[6],i[7],dest[index]))
                    break
            elif signs[index]=='>':
                if interval[4] < nums[index] < interval[5]:
                    intervals.remove(interval)
                    i = interval
                    intervals.append((i[0],i[1],i[2],i[3],nums[index]+1,i[5],i[6],i[7],dest[index]))
                    intervals.append((i[0],i[1],i[2],i[3],i[4],nums[index],i[6],i[7],i[8]))
                    break
            elif signs[index]=='.':
                intervals.remove(interval)
                intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
                break

        elif p=='s':
            if signs[index]=='<':
                if interval[6] < nums[index] < interval[7]:
                    intervals.remove(interval)
                    i = interval
                    intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],nums[index],i[7],i[8]))
                    intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],nums[index]-1,dest[index]))
                    break
            elif signs[index]=='>':
                if interval[6] < nums[index] < interval[7]:
                    intervals.remove(interval)
                    i = interval
                    intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],nums[index]+1,i[7],dest[index]))
                    intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],nums[index],i[8]))
                    break
            elif signs[index]=='.':
                intervals.remove(interval)
                intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
                break
        else: 
            intervals.remove(interval)
            intervals.append((i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],dest[index]))
            break
    return 0
while intervals != []:
    total += check_rule_interval(intervals[0])
print(total)