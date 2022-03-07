from collections import OrderedDict


f = open('input.txt')
input = {}
start = ""

for line in f:
    line = line.strip()
    if "->" in line:
        line = line.split('->')
        input[line[0].strip()] = line[1].strip()
    elif line != "":
        start = line
        
#print(input)

combos = OrderedDict()
for i in range(0, len(start)-1):
    if start[i:i+2] in combos:
        combos[start[i:i+2]] += 1
    else:
        combos[start[i:i+2]] = 1

#print(combos)
for k in range(0,40):
    combos_temp = OrderedDict()
    for k,v in combos.items():
        if k in input:
            if k[0]+input[k] in combos_temp:
                combos_temp[k[0]+input[k]] += v
            else:
                combos_temp[k[0]+input[k]] = v
                
            if input[k]+k[1] in combos_temp:
                combos_temp[input[k]+k[1]] += v
            else:
                combos_temp[input[k]+k[1]] = v
                
    combos = combos_temp
    

i = 0
count_chars = {}
for k,v in combos.items():
    if i == 0:
        if k[0] in count_chars:
            count_chars[k[0]] += 1
        else:
            count_chars[k[0]] = 1 
            
        i += 1

    if k[1] in count_chars:
        count_chars[k[1]] += v
    else:
        count_chars[k[1]] = v
        
        

all_values = count_chars.values()
max_value = max(all_values)

min_value = min(all_values)

#print(combos)
#print(count_chars)
print('Part 1')
print(max_value, min_value, max_value-min_value)
print('====================================')
print('Part 2')
