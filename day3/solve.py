#Part 1
LENGTH_INPUT_LINE = 12

f = open('input.txt')
x_pos = 0
y_pos = 0
countOnes = [0]*LENGTH_INPUT_LINE
lines = []

# O(n), n = # of input lines
for line in f:
    for i in range(0, len(line)-1):
        countOnes[i] = countOnes[i]+1 if line[i]=="1" else countOnes[i]
    lines.append(line.strip())

gamma = 0
epsilon = 0
bit = LENGTH_INPUT_LINE-1

#O(1), 12 iterations
for i in range(0, LENGTH_INPUT_LINE):
    if countOnes[i] > (len(lines)/2):
        gamma += pow(2, bit)
    else:
        epsilon += pow(2, bit)
    bit -= 1
    
print("Part 1")
print("Epsilon:", epsilon," Gamma:", gamma," Value:", epsilon*gamma)
#total O(n)

print("====================================")
print("Part 2")
#Part 2
#use countOnes
values = []
lines_co2_scrubber = lines
lines_oxygen_generator = lines.copy()
count_ones_co2_scrubber = countOnes
count_ones_oxygen_generator = count_ones_co2_scrubber.copy()
to_remove = []

#oxygen_generator
for i in range(0, LENGTH_INPUT_LINE):
    if len(lines_oxygen_generator) == 1:
        break
    for l in lines_oxygen_generator:
        #oxygen generator (favorable to 1)
        if len(lines_oxygen_generator) == 1:
            break
        if not ((count_ones_oxygen_generator[i] >= (len(lines_oxygen_generator)/2) and l[i] == "1") or (count_ones_oxygen_generator[i] < (len(lines_oxygen_generator)/2) and l[i] == "0")):
            for j in range(i+1, LENGTH_INPUT_LINE):
                count_ones_oxygen_generator[j] = count_ones_oxygen_generator[j]-1 if l[j] == "1" else count_ones_oxygen_generator[j]
            to_remove.append(l)
            
    lines_oxygen_generator = [x for x in lines_oxygen_generator if x not in to_remove]
    to_remove = []
    #print(lines_oxygen_generator)
    #print("Current column:", i, "   Rows:", len(lines_oxygen_generator))
    
            

#co2 scrubber
for i in range(0, LENGTH_INPUT_LINE):
    if len(lines_co2_scrubber) == 1:
        break
    for l in lines_co2_scrubber:
        #co2 scrubber (favorable to 0)
        if len(lines_co2_scrubber) == 1:
            break
        if not ((count_ones_co2_scrubber[i] < (len(lines_co2_scrubber)/2) and l[i] == "1") or (count_ones_co2_scrubber[i] >= (len(lines_co2_scrubber)/2) and l[i] == "0")):
            for j in range(i+1, LENGTH_INPUT_LINE):
                count_ones_co2_scrubber[j] = count_ones_co2_scrubber[j]-1 if l[j] == "1" else count_ones_co2_scrubber[j]
            to_remove.append(l)
            
    lines_co2_scrubber = [x for x in lines_co2_scrubber if x not in to_remove]
    to_remove = []
    #print(lines_co2_scrubber)
        
co2_scrubber_value = 0
oxygen_generator_value = 0
bit = LENGTH_INPUT_LINE - 1

for i in range(0, LENGTH_INPUT_LINE):
    if lines_co2_scrubber[0][i] == "1":
        co2_scrubber_value += pow(2, bit)
    
    if lines_oxygen_generator[0][i] == "1":
        oxygen_generator_value += pow(2, bit)
    bit -= 1
    
# 3399 1249
# 110101000111 oxy
# 010011100001 co2
print("co2: ",lines_co2_scrubber[0],"oxy:", lines_oxygen_generator[0])
print("co2: ",co2_scrubber_value, " oxy:", oxygen_generator_value, " value:", oxygen_generator_value*co2_scrubber_value)

