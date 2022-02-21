#Part 1
f = open('input.txt')
x_pos = 0
y_pos = 0

#O(n), n = number of input lines
for line in f:
    command = line.split(' ')
    
    if command[0] == "up":
        y_pos -= int(command[1])
    elif command[0] == "down":
        y_pos += int(command[1])
    else:
        x_pos += int(command[1])
        
print("Part 1")   
print("x:", x_pos, " y:", y_pos, " Position: ", x_pos*y_pos)

#Part 2
f = open('input.txt')
x_pos = 0
y_pos = 0
aim = 0

#O(n), n = number of input lines
for line in f:
    command = line.split(' ')
    
    if command[0] == "up":
        aim -= int(command[1])
    elif command[0] == "down":
        aim += int(command[1])
    else:
        x_pos += int(command[1])
        y_pos += (aim * int(command[1]))
        
print("===============================")
print("Part 2")   
print("x:", x_pos,"y:", y_pos,"aim:", aim)
print("Position: ", x_pos*y_pos)
    