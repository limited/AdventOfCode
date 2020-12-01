#!/usr/bin/env python3
# Started 9:14AM
# Part1: 9:41, ugh!
# Part2: 10:02, not bad

from collections import defaultdict
infile = 'game_input'
#infile = 'test_1'

def main():
    local_map = [l.rstrip().split(')') for l in open(infile, 'r').readlines()]
    #print(local_map)

    o_graph = dict() 
    for orbit in local_map:
        o_graph[orbit[1]] = orbit[0]
    #print(o_graph)
        

    orbits = 0
    for k in o_graph:
        #print("Counting from ",k)
        
        while k != 'COM':
            orbits += 1
            #print(f"k {k} c {orbits}")
            k = o_graph[k]

    print(orbits)

    # Part 2
    my_obj = o_graph['YOU']
    san_obj = o_graph['SAN']
    #my_obj = 'K'
    #san_obj = 'I'
    print(my_obj, san_obj)

    og2 = defaultdict(list)
    for orbit in local_map: # Make bidir
        og2[orbit[0]].append(orbit[1])
        og2[orbit[1]].append(orbit[0])
    #print(og2)

    count_xfer(og2, my_obj, san_obj)

# Shortest path via BFS    
def count_xfer(o_graph, start, dest):
    visited = []
    queue = []
    depths = dict() # Distances from start

    queue.append(start)
    visited.append(start)
    depths[start] = 0
    
    while queue:
        next = queue.pop(0)
        #print("Next", next)
        for i in o_graph[next]:
            depths[i] = depths[next] + 1
            if i == dest:
                print ("Found",i)
                print (depths[i])
                return
            
            if i not in visited:
                queue.append(i)
                visited.append(i)
        #print("Q",queue)
    
if __name__ == '__main__':
    main()
