## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02b_vector:: sqrt(), atan2(), function

import math

X, Y = map(int, input().split())

def distance(xx, yy):
    return math.sqrt(xx*xx + yy*yy)

def direction( xx, yy):
    return math.degrees(math.atan2(xx, yy))

dst = distance(X, Y)
dir = direction(X, Y)

print(f'{dst = }, {dir = }')

# =========================================================
# *** list of input lines ***
'''
X Y

[Case a]
3 4 

[Case b]
-4 3

[Case c]
-3 -4

[Case d]
4 -3

'''

