## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02c_vector:: sqrt(), atan2(), function

import math

X, Y = map(int, input().split())

def vector(xx, yy):
    return (
        math.sqrt(xx*xx + yy*yy),
        math.degrees(math.atan2(xx, yy)) )

dst, dir = vector(X, Y)

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

