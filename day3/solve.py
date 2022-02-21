#Part 1
LENGTH_INPUT_LINE = 5

f = open('testinput.txt')
x_pos = 0
y_pos = 0
countOnes = [0]*LENGTH_INPUT_LINE
numLines = 0
lines = []

# O(n), n = # of input lines
for line in f:
    for i in range(0, len(line)-1):
        countOnes[i] = countOnes[i]+1 if line[i]=="1" else countOnes[i]
    numLines += 1
    lines.append(line)
    
gamma = 0
epsilon = 0
bit = LENGTH_INPUT_LINE-1

#O(1), 12 iterations
for i in range(0, LENGTH_INPUT_LINE):
    if countOnes[i] > (numLines/2):
        gamma += pow(2, bit)
    else:
        epsilon += pow(2, bit)
    bit -= 1
        
print(epsilon, gamma, epsilon*gamma)
#total O(n)


#Part 2
#use countOnes

co2_scrubber_value_found = False
oxygen_generator_value_found = False
values = []

#oxygen_generator
for l in lines:
    if oxygen_generator_value_found:
        break
    
    for i in range(0, LENGTH_INPUT_LINE):
        
        #oxygen generator (favorable to 1)
        if countOnes[i] >= (numLines/2) and l[i] == "1":
            if i == LENGTH_INPUT_LINE - 1:
                oxygen_generator_value_found = True
                print("found ", l)
                values.append(l)

        elif countOnes[i] < (numLines/2) and l[i] == "0":
            if i == LENGTH_INPUT_LINE - 1:
                oxygen_generator_value_found = True
                print("found ", l)
                values.append(l)
        else:
            print("skipping ", l, " at ", i)
            break
            

#co2 scrubber
for l in lines:
    if co2_scrubber_value_found:
        break
    
    for i in range(0, LENGTH_INPUT_LINE):
        #co2 scrubber (favorable to 0)
        if countOnes[i] < (numLines/2) and l[i] == "1":
                co2_scrubber_value_found = True
                print("found co2 ", l)
                values.append(l)

        elif countOnes[i] >= (numLines/2) and l[i] == "0":
            if i == LENGTH_INPUT_LINE - 1:
                co2_scrubber_value_found = True
                print("found co2 ", l)
                values.append(l)

        else:
            break
        
if oxygen_generator_value_found == False:
    values.append(lines[len(lines)-1])
if co2_scrubber_value_found == False:
    values.append(lines[len(lines)-1])
        
print(values)

