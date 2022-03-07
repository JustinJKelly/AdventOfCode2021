f = open('input.txt')
input = []

for line in f:
    input.append(line.strip())
    

def getMinimumPath(x, y, input):
    #print('efed')
    if x > len(input) - 1 or y > len(input) - 1:
        return float('inf')
    else:
        if x == len(input)-1 and y == len(input)-1:
            return 0
        else:
            return min(int(input[x][y]) + getMinimumPath(x+1, y, input), int(input[x][y]) + getMinimumPath(x, y+1, input))

print(getMinimumPath(0,0,input))
print('Part 1')
print('====================================')
print('Part 2')
