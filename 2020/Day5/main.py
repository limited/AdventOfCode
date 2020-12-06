#!/usr/bin/env python3

t = {"F": "0", "B": "1", "L": "0", "R":"1"}
def binc(l):
    return  int("".join([t[i] for i in l]), 2)


with open('game_input', 'r') as f:
    all_seats = list()    
    for l in f:
        l = l.rstrip()
        row = binc(l[0:7])
        col = binc(l[7:10])
        seat = row*8+col
        all_seats.append(seat)

    print(max(all_seats))

    all_seats = sorted(all_seats)
    for (i,s) in enumerate(all_seats):
        if i>0 and i < len(all_seats)-1 and s-1 != all_seats[i-1]:
            print(s-1)

    


    

    
