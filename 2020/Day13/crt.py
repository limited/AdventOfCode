#!/usr/bin/env python3

import math


def mod_inv(n, mod):
    print("mod_inv", n, mod)
    x = n % mod    
    for i in range(1, mod):
        if x*i % mod == 1:
            return i

# Gonna use the CRT here
# sum over remainder_i*n_i*x_i
# where n_i = product of other modulos
# and x_i is modular inverse of n_i
# vals is [(rem_1, mod_1), (rem_2, mod_2), ...]
def crt(vals):
    mods = [v[1] for v in vals]
    rems = [v[0] for v in vals]
    print(mods, rems)
    
    N = math.prod(mods)
    total = 0
    for idx,r in enumerate(rems):
        n = int(N/mods[idx])
        x = mod_inv(n, mods[idx])
        total += r*n*x
    return (total % N)

