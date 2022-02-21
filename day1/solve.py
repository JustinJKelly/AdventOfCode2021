
#Part 1
f = open('input.txt')
prev = float('-inf')
count_part1 = 0

#O(n)
for line in f:
    v = int(line)
    if prev < v:
        count_part1 += 1
        
    prev = v
    
print("Part 1\ncount:", count_part1-1)

#Part 2
f = open('input.txt')
prev = float('-inf')
v1 = 0
v2 = 0
v3 = 0
i = 1
count_part2 = 0

#O(n)
for line in f:
    v = int(line)
    if i == 1:
        v1 += v
    elif i == 2:
        v1 += v
        v2 += v 
    else:
        v1 += v
        v2 += v 
        v3 += v
    
    if i > 3:
        if i % 3 == 0:
            count_part2 = count_part2+1 if v1 > prev else count_part2
            prev = v1
            v1 = 0
        elif i % 3 == 1:
            count_part2 = count_part2+1 if v2 > prev else count_part2
            prev = v2
            v2 = 0
        else:
            count_part2 = count_part2+1 if v3 > prev else count_part2
            prev = v3
            v3 = 0
    
    i += 1

print("===============================")
print("Part 2:\ncount: ", count_part2)
    
