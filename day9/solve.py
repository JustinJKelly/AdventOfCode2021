f = open('input.txt')
input = []

for line in f:
    line = line.strip()
    input.append(list(line))
    
low_points = 0
all_low_points = []
sum_of_the_low_points = 0
#low_points_counts = {}
for i in range(0, len(input)):
    for j in range(0, len(input[i])):
        prev_low_points = low_points
        c = input[i][j] 
        if i == 0 and j == 0:
            low_points = low_points+1 if (input[i+1][j] > c and input[i][j+1] > c) else low_points
        elif i == 0 and j == len(input[i])-1:
            low_points = low_points+1 if (input[i+1][j] > c and input[i][j-1] > c) else low_points
        elif i == 0:
            low_points = low_points+1 if (input[i+1][j] > c and input[i][j+1] > c and input[i][j-1] > c) else low_points
        elif j == 0 and i == len(input)-1:
            low_points = low_points+1 if (input[i-1][j] > c and  input[i][j+1] > c) else low_points
        elif j == 0:
            low_points = low_points+1 if (input[i-1][j] > c and input[i][j+1] > c and input[i+1][j] > c) else low_points
        elif i == len(input)-1 and j == len(input[i])-1:
            low_points = low_points+1 if (input[i-1][j] > c and input[i][j-1] > c) else low_points
        elif i == len(input)-1:
            low_points = low_points+1 if (input[i-1][j] > c and input[i][j-1] > c and input[i][j+1] > c) else low_points
        elif j == len(input[i])-1:
            low_points = low_points+1 if (input[i-1][j] > c and input[i][j-1] > c and input[i+1][j] > c) else low_points
        else:
            low_points = low_points+1 if (input[i-1][j] > c and input[i][j+1] > c and input[i+1][j] > c and input[i][j-1] > c) else low_points

        if low_points > prev_low_points:
            '''if input[i][j] in low_points_counts:
                low_points_counts[input[i][j]] += 1
            else:
                low_points_counts[input[i][j]] = 1'''
                
            sum_of_the_low_points += (int(input[i][j]) + 1)   
            all_low_points.append((i,j))
                                 


print("Part 1")
print("Number of low points:", low_points)
print("Sum of the Low Points:", sum_of_the_low_points)
print("====================================")
print("Part 2")

#find basins
basins = []
    
#print(len(visited), len(visited[0]))
for lp in all_low_points:
    visited = []
    for i in range(0,len(input)):
        visited.append([0]*len(input[i]))
    
    x = lp[0]
    y = lp[1]
    
    stack = []
    basin = []
    
    stack.append((int(x),int(y)))
    
    while len(stack) > 0:
        curr = stack.pop()
        if visited[curr[0]][curr[1]] == 1:
            continue
        basin.append(input[curr[0]][curr[1]])
        visited[curr[0]][curr[1]] = 1
            
        v = input[curr[0]][curr[1]]

        if (curr[0]-1 >= 0) and (input[curr[0]-1][curr[1]] != "9"): #(x-1, y)
            stack.append((curr[0]-1,curr[1]))
        if (curr[1]+1 < len(input[0])) and (input[curr[0]][curr[1]+1] != "9"): #(x, y+1)
            stack.append((curr[0],curr[1]+1))
        if (curr[0]+1 < len(input)) and (input[curr[0]+1][curr[1]] != "9"): #(x+1, y)
            stack.append((curr[0]+1,curr[1]))
        if (curr[1]-1 >= 0) and (input[curr[0]][curr[1]-1] != "9"): #(x, y-1)
            stack.append((curr[0],curr[1]-1))
            
    basins.append(basin)
            
basins = sorted(basins, key=lambda x: len(x), reverse=True)
part2 = 1
for i in range(0,3):
    part2 *= len(basins[i])

    
print("Part2:", part2)

