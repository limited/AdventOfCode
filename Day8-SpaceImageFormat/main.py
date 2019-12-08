#!/usr/bin/env python3
#      --------Part 1--------   --------Part 2--------
#Day       Time   Rank  Score       Time   Rank  Score
#  8   08:40:33   9417      0   09:46:27   9126      0

from collections import Counter

def render(layers, pixel):
    for i in range(0, len(layers)):
        if layers[i][pixel] != '2':
            return layers[i][pixel]
        
# Part1
filein = open('game_input', 'r').read()
layer_size = 25*6
layers = [filein[x:x+layer_size] for x in range(0, len(filein)-1, layer_size)]
counts = [Counter(i) for i in layers]
min_counts = {c['0'] : c['1']*c['2'] for c in counts}
print(min_counts[min(min_counts.keys())])

# Part2
rendered = [render(layers, i) for i in range(0, layer_size)]
while len(rendered):
    print(rendered[0:25])
    rendered = rendered[25:]
    
AURCY
