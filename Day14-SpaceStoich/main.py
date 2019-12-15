#!/usr/bin/env python3

from collections import defaultdict

def read_inputs(filename):
    r_rxn = dict()
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
        
            
        

def main():
#    rev_rxn = read_inputs('test1')
    rev_rxn = read_inputs('game_input')    
    print(rev_rxn)

    need = defaultdict(int)
    need['FUEL'] = 1
    waste = defaultdict(int)
    ore_count = 0
    
    while len(need) > 0:
        print(f"Need: {need}")
        cur_el = next(iter(need))
        cur_need = need[cur_el]
        print(f"-------Need {cur_need} of {cur_el}-------")
        print(f"Waste: {waste}")

        if cur_el == 'ORE':
            ore_count += cur_need
            del need['ORE']
            continue
        
        #consume waste first
        if cur_el in waste:
            if waste[cur_el] > cur_need:
                waste[cur_el] -= cur_need
                del need[cur_el]
                print(f"Consuming partial of waste, {waste[cur_el]} remain")
                continue
            
            elif waste[cur_el] == cur_need:
                del need[cur_el]
                del waste[cur_el]
                print("Consuming all of waste")
                continue
            
            else:
                need[cur_el] -= waste[cur_el]
                del waste[cur_el]
                cur_need = need[cur_el]
                print (f"Consuming all of waste, {need[cur_el]} remain")


        out_qty = rev_rxn[cur_el]['outqty']
        if cur_need > out_qty:
            need[cur_el] -= out_qty
            print(f"Produces {out_qty}, {need[cur_el]} remain")
            
        elif cur_need == out_qty:
            print(f"{cur_el} Satisfied exactly")
            del need[cur_el]
            
        else:
            waste[cur_el] += out_qty - cur_need
            del need[cur_el]
            print(f"Waste {waste[cur_el]} produced")
            
        for (qty, elem) in rev_rxn[cur_el]['inputs'].items():
            print(f"Need addl {qty} of {elem}")
            need[qty] += elem

    print("ORE COUNT", ore_count)
    
if __name__ == '__main__':
    main()
