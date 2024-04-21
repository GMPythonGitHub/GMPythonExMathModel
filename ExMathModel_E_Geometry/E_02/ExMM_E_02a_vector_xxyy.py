## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02a_vector_xxyy:: sqrt(), atan2()

import math

X, Y = map(int, input().split())

rr = math.sqrt(X**2 + Y**2)
th = math.degrees(math.atan2(Y, X))

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

