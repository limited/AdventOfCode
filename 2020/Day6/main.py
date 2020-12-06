#!/usr/bin/env python3

with open('game_input', 'r') as f:
    f = [len(set(l.replace("\n", ""))) for l in f.read().split('\n\n')]
    print(sum(f))

    

from collections import Counter
with open('game_input', 'r') as f:
    all_count = 0
    for group in f.read().split('\n\n'):
        gc = Counter(group+"\n")
        for ans in gc.keys():
            if ans != '\n' and gc[ans] == gc['\n']:
                all_count += 1

    print(all_count)

