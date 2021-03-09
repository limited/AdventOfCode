#!/usr/bin/env python3

test = "1 + (2 * 3) + (4 * (5 + 6))"

def comp(test, depth):
    i = 0
    while len(test) > 0:
        if test is None:
            return 0
        
        if test[i] == ' ':
            test = test[1:]
            continue
        
        if test[i] == '(':
            print("Pushing", depth+1)
            test = comp(test[i+1:], depth+1)
            
        elif test[i] == ')':

            return test[i+1:]

        test = test[1:]
            
        

print(comp(test.rstrip(), 0))
