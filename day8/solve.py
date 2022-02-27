
f = open('input.txt')
input = []
output = []

for line in f:
    line = line.strip()
    input_output = line.split(' | ')
    input.append(input_output[0])
    output.append(input_output[1])

count_1_4_7_8 = 0

#Part 1
for l in output:
    for s in l.split(' '):
        if len(s) in [2,3,4,7]:
            count_1_4_7_8 += 1
    
    
def findDigitValues(m, output):
    
    s = set(['a','b','c','d','e','f','g'])
    segments = {}
    segments["top"] = [x for x in m[3] if x not in m[2]][0]
    segments["middle"] = [x for x in m[5] if x in m[4]][0]
    segments["bottom_right"] = [x for x in m[6] if x in m[2]][0]
    segments["top_right"] = [x for x in m[2] if x not in [segments["bottom_right"]]][0]
    segments["top_left"] = [x for x in m[4] if x not in [segments["bottom_right"],segments["middle"],segments["top_right"]]][0]
    
    for v in segments.values():
        if v in s:
            s.discard(v)
            
    segments["bottom"] = [x for x in m[5] if x in s][0]
    s.discard(segments["bottom"])
    segments["bottom_left"] = list(s)[0]
    
    value = []
    
    output = output.split(" ")
    for o in output:
        if sorted(o) == sorted([segments["top_right"], segments["bottom_right"]]): #1
            value.append("1")
        elif sorted(o) == sorted([segments["top"], segments["top_right"], segments["middle"], segments["bottom_left"],segments["bottom"]]): #2
            value.append("2")
        elif sorted(o) == sorted([segments["top"], segments["top_right"], segments["middle"], segments["bottom_right"],segments["bottom"]]): #3
            value.append("3")
        elif sorted(o) == sorted([segments["top_right"], segments["middle"], segments["top_left"],segments["bottom_right"]]): #4
            value.append("4")
        elif sorted(o) == sorted([segments["top"], segments["top_left"], segments["middle"], segments["bottom_right"],segments["bottom"]]): #5
            value.append("5")
        elif sorted(o) == sorted([segments["top"], segments["top_left"], segments["middle"], segments["bottom_left"], segments["bottom_right"], segments["bottom"]]): #6
            value.append("6")
        elif sorted(o) == sorted([segments["top"], segments["top_right"], segments["bottom_right"]]): #7
            value.append("7")
        elif sorted(o) == sorted([segments["top"], segments["top_right"], segments["top_left"], segments["middle"], segments["bottom_left"],segments["bottom_right"],segments["bottom"]]): #8
            value.append("8")
        elif sorted(o) == sorted([segments["top"], segments["top_right"], segments["top_left"], segments["middle"], segments["bottom_right"],segments["bottom"]]): #9
            value.append("9")
        elif sorted(o) == sorted([segments["top"], segments["top_right"], segments["top_left"], segments["bottom_left"],segments["bottom_right"],segments["bottom"]]): #0
            value.append("0")
    
    return int(''.join(value))
    
count_part2 = 0
#Part 2
for i in range(0, len(input)):
    i_input = input[i]
    i_output = output[i]

    m = {}
    for l in i_input.split(' '):
        if len(l) not in m:
            m[len(l)] = []
        m[len(l)].append(l)
        
        
    m_common = {}
    for k,v in m.items():
        m_common[k] = set.intersection(*[set(list) for list in v])
         
    count_part2 += findDigitValues(m_common, i_output)

    
    
print("Part 1")
print("Count:", count_1_4_7_8)

print("====================================")
print("Part 2")
print("Count:", count_part2)