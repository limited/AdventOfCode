#!/usr/bin/env python3


with open('game_input', 'r') as f:
    #print([p for p in f.read().split('\n\n')])
    #print([len(p.replace("\n", " ").split(" ")) for p in f.read().split('\n\n')])

    #print([1 if len(p.replace("\n", " ").split(" ")) == 8 or \
    #            (len(p.replace("\n", " ").split(" ")) == 7 and "cid:" not in p) else 0\
    #       for p in f.read().split('\n\n')])

    print(sum([1 if len(p.replace("\n", " ").split(" ")) == 8 or \
           (len(p.replace("\n", " ").split(" ")) == 7 and "cid:" not in p) else 0\
           for p in f.read().split('\n\n')]))

# Part2

def int_between(di, field, low, hi):
    return field in di and int(di[field]) >= low and int(di[field]) <= hi

def verify_hgt(hgt):
    try:
        if "cm" in hgt:
            h = int(hgt[0:3])
            return h >= 150 and h <=193
        else:
            h = int(hgt[0:2])
            return h >=59 and h <= 76
    except:
        return False

def verify_hcl(hcl):
    if hcl[0] != '#':
        return False
    
    if len(hcl) != 7:
        return False
    
    chrs = [ord(a) for a in hcl[1:]]
    return all([(a >=48 and a<=57) or (a >=97 and a<=102) for a in chrs])

def is9int(i):
    try:
        a=int(i)
        return len(i)==9
    except:
        return False


with open('game_input', 'r') as f:
    pp = [p.replace("\n", " ") for p in f.read().split('\n\n')]
    recs = list()

    for p in pp:
        fields = p.split(" ")
        d = {i.split(":")[0]:i.split(":")[1] if len(i) > 0 else None for i in fields}
        recs.append(d)
        
    valid = filter(lambda pp: int_between(pp, "byr", 1920, 2002), recs)

    valid = filter(lambda pp: int_between(pp, "iyr", 2010, 2020), valid)
    
    valid = filter(lambda pp: int_between(pp, "eyr", 2020, 2030), valid)
    
    valid = filter(lambda pp: 'hgt' in pp and verify_hgt(pp['hgt']), valid)

    valid = filter(lambda pp: 'hcl' in pp and verify_hcl(pp['hcl']), valid)
    
    valid = filter(lambda pp: 'ecl' in pp and pp['ecl'] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], valid)
    
    valid = filter(lambda pp: 'pid' in pp and is9int(pp['pid']), valid)
    #valid = [i for i in valid]
    #print(len(valid), valid)
    #import sys;sys.exit(0)
    
    #print([i for i in valid])
    print(len([i for i in valid]))
        

        
#    print(pp)
