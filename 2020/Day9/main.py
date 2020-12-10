#!/usr/bin/env python3

lookback=25
#lookback=5
with open('game_input', 'r') as f:
    nums = [int(l.rstrip()) for l in f.read().split('\n')]

def find_prev_sum(lb, target):
    found = False
    for i in lb:
        if target-i != i and target-i in lb:
            found = True
            
    return(found)

# Returns end_idx where sum(nums[start_idx]..nums[end_idx] == target) or None
def get_contig_sum(nums, start_idx, target):
    for i in range(0, len(nums)-start_idx):
        rng = nums[start_idx:start_idx+i]
        s = sum(rng) 
        if s == target:
            print(min(rng)+max(rng))
            return True

        elif s > target:
            # Bail early, will never find it starting here
            return None
        
    return None


# Part 1    
for i in range(lookback, len(nums)):
    if not find_prev_sum(nums[i-lookback:i], nums[i]):
        contig_target = nums[i]
        break

print(contig_target)

# Part 2
for i in range(0, len(nums)):
    end_idx = get_contig_sum(nums, i, contig_target)
    if end_idx is not None:
        break
    
    


               
