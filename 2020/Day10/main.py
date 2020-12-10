#!/usr/bin/env python3
from collections import Counter

with open('game_input', 'r') as f:
    jolts = sorted([int(l.rstrip()) for l in f.read().split('\n')])


# Part 1
jolts.insert(0, 0)
jolts.append(jolts[-1]+3) # Sorted so last element is always the max
dist = Counter([jolts[i]-jolts[i-1] for i in range(1,len(jolts))])
print(dist[1]*dist[3])

# Part 2

combo_cache = dict() #memoization
def count_combos(jolts):
    if len(jolts) == 1: 
        return (1)

    first = jolts[0]
    if first in combo_cache:
        return combo_cache[first]

    # Works but I like the expanded version more
    #combos = sum([count_combos(jolts[k:]) if (jolts[k] - first <= 3) else 0 for k in range(1, len(jolts))])
    
    combos = 0
    for k in range(1, len(jolts)):
        if (jolts[k] - first <= 3):
            #print(first, " checking next ", jolts[k])
            combos += count_combos(jolts[k:])
    
        else:
            break

    combo_cache[first] = combos
    return (combos)

print(count_combos(jolts))
