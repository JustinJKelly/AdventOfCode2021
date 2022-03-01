#!/bin/bash

day=$1
mkdir "day${day}"
touch "day${day}"/spec_part1.txt "day${day}"/spec_part2.txt "day${day}"/testinput.txt "day${day}"/input.txt "day${day}"/solve.py
echo "f = open('input.txt')

for line in f:
    print(line)
    

print('Part 1')
print('====================================')
print('Part 2')" >> "day${day}"/solve.py