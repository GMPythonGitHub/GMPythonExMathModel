## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02c_vector:: sqrt(), atan2(), function

import math

X, Y = map(int, input().split())

def vector_xxyy(xx, yy):
    return (
        math.sqrt(xx**2 + yy**2),
        math.degrees(math.atan2(xx, yy)) )

rr, th = vector_xxyy(X, Y)

print(f'{rr = }, {th = }')

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

