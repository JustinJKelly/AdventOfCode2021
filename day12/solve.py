f = open('input.txt')
input = []

for line in f:
    input.append(line.strip())
    
adjList = {}

for l in input:
    vertices = l.split('-')
    
    if vertices[0] in adjList:
        adjList[vertices[0]].append(vertices[1])
    else:
        adjList[vertices[0]] = [vertices[1]]
        
    if vertices[1] in adjList:
        adjList[vertices[1]].append(vertices[0])
    else:
        adjList[vertices[1]] = [vertices[0]]
        
print(adjList)

stack = [('start', ['start'])]
paths = []
while len(stack) > 0:
    curr = stack.pop()
    for v in adjList[curr[0]]:
        if v not in curr[1] or v[0].isupper():
            if v == "end":
                paths.append(curr[1]+[v])
            else:
                stack.append((v, curr[1]+[v]))
        else:
            continue   
        
    
#for p in paths:
#    print(p)
    
print(len(paths))
print('Part 1')
print('====================================')
print('Part 2')


def checkCountSmallCaves(l):
    visited = []
    
    for i in l:
        if i[0].islower() and i in visited:
            return False
        else:
            visited.append(i)
    return True

stack = [('start', ['start'])]
paths = []
while len(stack) > 0:
    curr = stack.pop()
    for v in adjList[curr[0]]:
        if v not in curr[1] or v[0].isupper() or checkCountSmallCaves(curr[1]) and v != "start":
            if v == "end":
                paths.append(curr[1]+[v])
            else:
                stack.append((v, curr[1]+[v]))
        else:
            continue   
        
#for p in paths:
    #print(p)
print(len(paths))
