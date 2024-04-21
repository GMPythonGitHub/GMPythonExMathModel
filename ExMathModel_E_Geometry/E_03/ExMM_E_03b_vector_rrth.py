## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03b_vector_rrth:: sqrt(), atan2(), function

import math

R, T = map(int, input().split())

def xx_comp(rr, th):
    return rr * math.cos(math.radians(th))
def yy_comp(rr, th):
    return rr * math.sin(math.radians(th))

xx = xx_comp(R, T)
yy = yy_comp(R, T)

print(f'{xx = }, {yy = }')

# =========================================================
# *** list of input lines ***
'''
L D

[Case a]
4 30 

[Case b]
4 150

[Case c]
12 -120

[Case d]
12 -45

'''

