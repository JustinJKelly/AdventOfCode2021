f = open('input.txt')
input = []
dist = []
visited = []

for line in f:
    input.append([int(x) for x in line.strip()])
    dist.append([float('inf')]*len(line.strip()))
    visited.append([0]*len(line.strip()))
    

s = []
s.append([0,0])
dist[0][0] = input[0][0]

while len(s) > 0:
    c = s.pop(0)
    
    if visited[c[0]][c[1]] == 1:
        continue
    
    if (c[0] < len(input[0]) - 1) and (input[c[0]+1][c[1]] + dist[c[0]][c[1]]) < dist[c[0]+1][c[1]]:
        dist[c[0]+1][c[1]] = input[c[0]+1][c[1]] + dist[c[0]][c[1]]
        s.append([c[0]+1,c[1]])
        
        
    if (c[1] < len(input) - 1) and (input[c[0]][c[1]+1] + dist[c[0]][c[1]]) < dist[c[0]][c[1]+1]:
        dist[c[0]][c[1]+1] = input[c[0]][c[1]+1] + dist[c[0]][c[1]]
        s.append([c[0],c[1]+1])
        
    visited[c[0]][c[1]] = 1
    
    #for d in dist:
    #    print(d)
    #print('\n\n')
    
#1163
#1381
#2136
#3694

for d in dist:
    print(d)
print('Part 1')
print(dist[len(input)-1][len(input)-1] - input[0][0])
print('====================================')
print('Part 2')
