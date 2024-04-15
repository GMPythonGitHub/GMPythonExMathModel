## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_04a_geom_point:: sqrt(), atan2()

import math

X, Y = map(int, input().split())

len = math.sqrt(X*X + Y*Y)
dir  = math.degrees(math.atan2(Y, X))

print(f'{len = }, {dir = }')

# =========================================================
# *** list of input lines ***
'''
X Y

[Case a]
3 4 

[Case b]
-3 -4

[Case c]
-3 -4

[Case d]
3 -4

'''

