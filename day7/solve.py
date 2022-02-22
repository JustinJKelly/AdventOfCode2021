import math 

f = open('input.txt')
input = []

for line in f:
    input = line.strip().split(',')
    
input = [int(k) for k in input]
input.sort()

mid = math.floor(len(input)/2)
fuel = 0
for i in input:
    if i != input[mid]:
        fuel += abs(i - input[mid])
    
print("Part 1")
print("Fuel:", fuel)

print("====================================")
print("Part 2")
#add numbers up until n ex: 3 -> 1+2+3
def sum_numbers_n(n):
    return n*(n+1)/2
    
best_fuel = float('inf')
for i in range(2000):
    score = 0
    for p in input:
        d = abs(p - i)
        score += sum_numbers_n(d)
        
    if score < best_fuel:
        best_fuel = score 

print("Fuel:", best_fuel)   


