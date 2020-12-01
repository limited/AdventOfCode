#!/usr/bin/env python3

# Took the hint on using a binary search on part2. Needed to make a key optimization to speed it up enough for that to be feasible

from collections import defaultdict

def read_inputs(filename):
    r_rxn = dict()
    fwd_rxn = dict()
    for l in open(filename, 'r'):
        (inz, outz) = l.rstrip().split('=>')
        
        indict = dict()
        for elem in inz.split(', '):
            (qty, el) = elem.rstrip().split(' ')
            indict[el] = int(qty)
            
        (qty, elem) = outz.lstrip().split(' ')
        r_rxn[elem] =  {'outqty': int(qty),
                       'inputs': indict}
        


    return r_rxn
        
def get_ore(rev_rxn, fuel):

    need = defaultdict(int)
    need['FUEL'] = fuel
    waste = defaultdict(int)
    ore_count = 0
    
    while len(need) > 0:
        #print(f"Need: {need}")
        cur_el = next(iter(need))
        cur_need = need[cur_el]
        #print(f"-------Need {cur_need} of {cur_el}-------")
        #print(f"Waste: {waste}")

        if cur_el == 'ORE':
            ore_count += cur_need
            del need['ORE']
            continue
        
        #consume waste first
        if cur_el in waste:
            if waste[cur_el] > cur_need:
                waste[cur_el] -= cur_need
                del need[cur_el]
                #print(f"Consuming partial of waste, {waste[cur_el]} remain")
                continue
            
            elif waste[cur_el] == cur_need:
                del need[cur_el]
                del waste[cur_el]
                #print("Consuming all of waste")
                continue
            
            else:
                need[cur_el] -= waste[cur_el]
                del waste[cur_el]
                cur_need = need[cur_el]
                #print (f"Consuming all of waste, {need[cur_el]} remain")


        out_qty = rev_rxn[cur_el]['outqty']
        times = 1
        if cur_need > out_qty:
            # WOW this optimization helped big time for part2!!
            #need[cur_el] -= out_qty

            times = cur_need // out_qty
            need[cur_el] -= out_qty * times
            #print(f"Need {cur_need} for {cur_el}, rxn produces {out_qty}, times={times}")
            
            #print(f"Produces {out_qty*times}, {need[cur_el]} remain")
            if need[cur_el] == 0:
                del need[cur_el]
            
        elif cur_need == out_qty:
            #print(f"{cur_el} Satisfied exactly")
            del need[cur_el]
            
        else:
            waste[cur_el] += out_qty - cur_need
            del need[cur_el]
            #print(f"Waste {waste[cur_el]} produced")
            
        for (elem, qty) in rev_rxn[cur_el]['inputs'].items():
            #print(f"Need addl {qty} of {elem}")
            need[elem] += (qty * times)

    return (ore_count)

def binary_search(rev_rxn, target, start, end):
    size = end-start
    if size == 0:
        return
    
    fuel = size//2
    val = get_ore(rev_rxn, start+fuel)
    print(f"Fuel: {start+fuel}, Start: {start}, End: {end}, Val: {val}")
    
    if val == target:
        print("JACKPOT {val}")
        return
    
    elif val < target:
        print("right")
        return binary_search(rev_rxn, target, int(start + size/2)+1, end)
    
    else:
        print("left")
        return binary_search(rev_rxn, target, start, int(start+size/2))
    
    

def main():
#    rev_rxn = read_inputs('test2')
    rev_rxn = read_inputs('game_input')    
    #print(rev_rxn)

    # Part1
    print("ore for 1 fuel", get_ore(rev_rxn, 1))

    # Part 2
    #Binary Search for fuel to return 1tril ore
    target_ore = 1000000000000
    max_fuel = 100000000 #XXX_EF maybe 10mil?
    binary_search(rev_rxn, target_ore, 1, max_fuel)

    #5194175 too high

    
if __name__ == '__main__':
    main()
