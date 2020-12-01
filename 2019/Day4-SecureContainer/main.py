#!/usr/bin/env python3
# Start Time: 7:42AM
# Part1: 7:57 


# Could do brute force OR find a way to build each
# gonna try brute force

def no_decrease(x):
    prev_c = None
    for c in str(x):
        if prev_c is None or c >= prev_c:
            prev_c = c
        else:
            return False
    return True

def has_adjacent(x):
    string = str(x)
    for i in range(0,len(string)):
        if i > 0 and string[i] == string[i-1]:
            return True

    return False

def count_adjacent(x):
    string = str(x)
    counts = {}

    inner_count = 1
    for i in range(1, len(string)+1):
        if i < len(string) and string[i] == string[i-1]:
            inner_count += 1
            #print(string[i], inner_count)            
        else:
            if inner_count > 0:
                counts[string[i-1]] = inner_count
                inner_count = 1
    return 2 in counts.values()
    
        
def main():
    #print(count_adjacent(113122))
    #return
    start = 248345
    end = 746315
    count = 0
    
    for x in range(start, end):
        if no_decrease(x):
               print(x,"nd")
        if has_adjacent(x) and no_decrease(x) and count_adjacent(x):
            count += 1

    print(f"Count: {count}")
    


if __name__ == '__main__':
    main()
