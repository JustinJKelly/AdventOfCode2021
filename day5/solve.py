
from numpy import diagonal


f = open('input.txt')
m = float('-inf')
vent_locations = []
diagonal_locations = []

for line in f:
    line = line.strip().split(" -> ")
    x1, y1 = line[0].split(',')
    x2, y2 = line[1].split(',')
    
    m = max(int(x1),int(y1),int(x2),int(y2),m)
    if x1 == x2 or y1 == y2:
        vent_locations.append([int(x1),int(y1),int(x2),int(y2)])
    else:
        diagonal_locations.append([int(x1),int(y1),int(x2),int(y2)])
    
map_vents = []
dangerous_spots = 0
for i in range(0, m+1):
    l = []
    for i in range(0, m+1):
        l.append(0)
    map_vents.append(l)
    
for coordinate in vent_locations:
    if coordinate[0] == coordinate[2]:
        #fixed x
        for i in range(min(coordinate[1], coordinate[3]), max(coordinate[1], coordinate[3])+1):
            map_vents[i][coordinate[0]] += 1
            dangerous_spots = dangerous_spots+1 if map_vents[i][coordinate[0]] == 2 else dangerous_spots
    else:
        #fixed y
        for i in range(min(coordinate[0], coordinate[2]), max(coordinate[0], coordinate[2])+1):
            map_vents[coordinate[1]][i] += 1
            dangerous_spots = dangerous_spots+1 if map_vents[coordinate[1]][i] == 2 else dangerous_spots
    
#print("Map Location:")
#for l in map_vents:
#    print(l)
print("Part 1")
print("Dangerous Spots:", dangerous_spots)


print("====================================")
print("Part 2")
    
for coordinate in diagonal_locations:
    if coordinate[0] == coordinate[2]:
        continue
    elif coordinate[1] == coordinate[3]:
        continue
    else: # diagonal
        if coordinate[0] > coordinate[2] and coordinate[1] > coordinate[3]:
            x = coordinate[0]
            y = coordinate[1]
            
            while x >= coordinate[2] and y >= coordinate[3]:
                map_vents[y][x] += 1
                dangerous_spots = dangerous_spots+1 if map_vents[y][x] == 2 else dangerous_spots
                x -= 1
                y -= 1
        elif coordinate[0] > coordinate[2] and coordinate[1] < coordinate[3]:
            x = coordinate[0]
            y = coordinate[1]
            
            while x >= coordinate[2] and y <= coordinate[3]:
                map_vents[y][x] += 1
                dangerous_spots = dangerous_spots+1 if map_vents[y][x] == 2 else dangerous_spots
                x -= 1
                y += 1
        elif coordinate[0] < coordinate[2] and coordinate[1] > coordinate[3]:
            x = coordinate[0]
            y = coordinate[1]
            
            while x <= coordinate[2] and y >= coordinate[3]:
                map_vents[y][x] += 1
                dangerous_spots = dangerous_spots+1 if map_vents[y][x] == 2 else dangerous_spots
                x += 1
                y -= 1
            
        elif coordinate[0] < coordinate[2] and coordinate[1] < coordinate[3]:
            x = coordinate[0]
            y = coordinate[1]
            
            while x <= coordinate[2] and y <= coordinate[3]:
                map_vents[y][x] += 1
                dangerous_spots = dangerous_spots+1 if map_vents[y][x] == 2 else dangerous_spots
                x += 1
                y += 1
                
print("Dangerous spots:",dangerous_spots)