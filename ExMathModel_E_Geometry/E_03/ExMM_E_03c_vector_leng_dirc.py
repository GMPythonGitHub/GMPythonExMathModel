## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03c_vector:: sqrt(), atan2(), function

import math

L, D = map(int, input().split())

def vector_rrth(rr, th):
    return (
        rr * math.cos(math.radians(th)),
        rr * math.sin(math.radians(th)) )

xx, yy = vector_rrth(L, D)

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

