#!/usr/bin/env python3


def contained_by(rules, search):
    out = list()
    for (k,v) in rules.items():
        if search in v:
            out.append(k)
    return(out)

def rec_contains_count(qty_rules, color):
    count = 0
    print("processing ", color)
    for (q,c) in qty_rules[color]:
        print(q,c)
        count += q
        count += q*rec_contains_count(qty_rules, c)

    print("---",count)
    return (count)
    

rules = dict()
qty_rules = dict()

with open('game_input', 'r') as f:
    for l in f:
        l = l.rstrip().split(" ")
        outer_color = " ".join(l[0:2])

        inside_colors = list()
        qty_inside = list()
        if l[4] != "no":
            for i in range(4, len(l), 4):
                qty = int(l[i])
                color = " ".join(l[i+1:i+3])
                inside_colors.append(color)
                qty_inside.append((qty, color))
        rules[outer_color] = inside_colors
        qty_rules[outer_color] = qty_inside


out = list()
queue = ['shiny gold']
while len(queue) > 0:
    for c in contained_by(rules, queue.pop(0)):
        if c not in out:
            out.append(c)
            queue.append(c)
print(len(out))

print(qty_rules)
print(rec_contains_count(qty_rules, 'shiny gold'))
