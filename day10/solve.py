
import math


f = open('input.txt')
input = []
for line in f:
    input.append(line.strip())
    
opening_chars = ['{','[', '<', '(']
closing_chars = ['}',']', '>', ')']
compare = {'{':'}', '[':']', '<':'>', '(':')'}
value_part1 = {'}':1197, ')':3, ']':57, '>':25137}

part1 = 0
first_bad_char = []
incompletes = []
for l in input:
    stack = []
    bad_line = False
    for i in range(0, len(l)):
        if l[i] in opening_chars:
            stack.append(l[i])
        else:    
            if len(stack) != 0:
                c = stack.pop()
                
                if compare[c] == l[i]:
                    continue
                else:
                    first_bad_char.append((l[i],i))
                    bad_line = True
                    part1 += value_part1[l[i]]
                    break
                
    if len(stack) != 0 and not bad_line:
        incompletes.append((l[i], i, stack))
                
                
                
print('Part 1')
print(part1)
print('====================================')
print('Part 2')

value_part2 = {'}':3, ')':1, ']':2, '>':4}
scores = []

incompletes = sorted(incompletes, key=lambda x: len(x[2]))            
for i in incompletes:
    s = 0
    for j in range(len(i[2])-1, -1, -1):
        s *= 5
        s += value_part2[compare[i[2][j]]]
    #print(s)
    scores.append(s)
        
scores.sort()
#print(scores)
print("Part2:", scores[math.floor(len(scores)/2)])
