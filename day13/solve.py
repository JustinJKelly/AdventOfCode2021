f = open('input.txt')
input = []
folds = []
max_x = 0
max_y = 0

for line in f:
    if line.strip() == "":
        continue
    elif "fold" in line:
        folds.append(line.strip())
    else:
        l = line.strip().split(',')
        input.append(l)
        max_x = max_x if max_x > int(l[0]) else int(l[0])
        max_y = max_y if max_y > int(l[1]) else int(l[1])
    
paper = []
for i in range(0,max_y+1):
    paper.append(['.']*(max_x+1)) 
    
for c in input:
    paper[int(c[1])][int(c[0])] = '#'
    

def foldX(x, paper):
    for j in paper:
        del j[x]
        
    index = x-1
    for i in range(0, len(paper)):
        for d in range(x,len(paper[i])):
            if paper[i][d] == "#":
                paper[i][index] = paper[i][d]
            index -= 1   
        index = x-1
        
    for j in range(0, len(paper)):
        paper[j] = paper[j][0:x]
        
    return paper
    
    
def foldY(y, paper):  
    del paper[y]
        
    index = y-1
    for i in range(y, len(paper)):
        for d in range(0,len(paper[i])):
            if paper[i][d] == "#":
                paper[index][d] = paper[i][d]  
        index -= 1
        
    return paper[0:y]

for f in folds:
    f = f.split(' ')
    fold = f[2].split('=')
    
    if fold[0] == 'y':
        paper = foldY(int(fold[1]), paper)
    else:
        paper = foldX(int(fold[1]), paper)
    
    #print('\n\n')
    #for l in paper:
    #    print(l)
    
    count = 0
    for l in paper:
        for c in l:
            count = count+1 if c == '#' else count
    #print(count)
        
print('Part 1')
print(count)
print('====================================')
print('Part 2')
file = open('output.txt', 'w')
for l in paper:
    file.write(str(l) + "\n")
    
file.close()
