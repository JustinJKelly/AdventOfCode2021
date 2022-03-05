f = open('input.txt')
input = []

flashes = 0
for line in f:
    l = list(line.strip())
    l = [int(c) for c in l]
    input.append(l)
    
first_step_all_flash = 0
for k in range(0,1000):
    
    if first_step_all_flash > 0:
        break
    
    stack = []
    for i in range(0,len(input)):
        for j in range(0,len(input)):
            input[i][j] += 1
            stack.append((i,j))
        
    while len(stack) > 0:
        curr = stack.pop()
        
        if input[curr[0]][curr[1]] == -1:
            continue
        
        if input[curr[0]][curr[1]] > 9:
            input[curr[0]][curr[1]] = -1
            flashes += 1
            
            if (curr[0]-1 >= 0 and curr[1]-1 >= 0) and input[curr[0]-1][curr[1]-1] > -1:
                input[curr[0]-1][curr[1]-1] += 1
                stack.append((curr[0]-1, curr[1]-1))
            if (curr[0]-1 >= 0) and input[curr[0]-1][curr[1]] > -1:
                input[curr[0]-1][curr[1]] += 1
                stack.append((curr[0]-1, curr[1]))
            if (curr[0]-1 >= 0 and curr[1]+1 < len(input)) and input[curr[0]-1][curr[1]+1] > -1:
                input[curr[0]-1][curr[1]+1] += 1
                stack.append((curr[0]-1, curr[1]+1))
            if (curr[1]+1 < len(input)) and input[curr[0]][curr[1]+1] > -1:
                input[curr[0]][curr[1]+1] += 1
                stack.append((curr[0], curr[1]+1))
            if (curr[0]+1 < len(input) and curr[1]+1 < len(input)) and input[curr[0]+1][curr[1]+1] > -1:
                input[curr[0]+1][curr[1]+1] += 1
                stack.append((curr[0]+1, curr[1]+1))
            if (curr[0]+1 < len(input)) and input[curr[0]+1][curr[1]] > -1:
                input[curr[0]+1][curr[1]] += 1
                stack.append((curr[0]+1, curr[1]))
            if (curr[0]+1 < len(input) and curr[1]-1 >= 0) and input[curr[0]+1][curr[1]-1] > -1:
                input[curr[0]+1][curr[1]-1] += 1
                stack.append((curr[0]+1, curr[1]-1))
            if (curr[1]-1 >= 0) and input[curr[0]][curr[1]-1] > -1:
                input[curr[0]][curr[1]-1] += 1
                stack.append((curr[0], curr[1]-1))
          
    num_flashes_step = 0
    for i in range(0,len(input)):
        for j in range(0,len(input[i])):
            if input[i][j] < 0:
                num_flashes_step += 1
                input[i][j] = 0
        
    if num_flashes_step == (len(input)*len(input)):
        first_step_all_flash = k+1
        break
    #print('\n\n')   
                
            
            
        
    
print('Part 1')
print("Flashes:", flashes)
print('====================================')
print('Part 2')
print("First step all flash:", first_step_all_flash)