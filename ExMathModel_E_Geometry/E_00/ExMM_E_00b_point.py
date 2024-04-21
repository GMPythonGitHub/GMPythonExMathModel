## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_00b_point:: sqrt(), atan2(), function

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

def distance(aa, bb):
    aax, aay = aa; bbx, bby = bb
    return math.sqrt((aax-bbx)**2 + (aay-bby)**2)

dist = distance(A, B)

print(f'{dist = }')

# =========================================================
# *** list of input lines ***
'''
Ax Ay
Bx By

[Case a]
0 0
4 3 

[Case b]
4 3
7 7

[Case c]
7 7
3 4

[Case d]
3 4
0 0

'''

