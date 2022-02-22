

def findNumFish(fish_map,iters):
    for i in range(0, iters):
        fish_map_temp = {}
        for k,v in fish_map.items():
            if k == "0":
                fish_map_temp["8"] = v
                if "6" in fish_map_temp:
                    fish_map_temp["6"] += v
                else:
                    fish_map_temp["6"] = v
            else:
                if str(int(k)-1) in fish_map_temp:
                    fish_map_temp[str(int(k)-1)] += v
                else:
                    fish_map_temp[str(int(k)-1)] = v
            
        fish_map = fish_map_temp
        
    return fish_map 
        
        
f = open('input.txt')
input = []
fish_map = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0}
for line in f:
    for v in line.split(','):
        v = v.strip()
        if v in fish_map:
            fish_map[v.strip()] += 1
        else:
            fish_map[v.strip()] = 1
    
fish_map_part2 = fish_map.copy()
#print(fish_map)
    
print("Part 1")
print("Num of Fish:", sum(findNumFish(fish_map,80).values()))

print("====================================")
print("Part 2")
print("Num of Fish:", sum(findNumFish(fish_map,256).values()))   
        