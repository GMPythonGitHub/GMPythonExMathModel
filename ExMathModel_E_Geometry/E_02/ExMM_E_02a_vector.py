## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02a_vector:: sqrt(), atan2()

import math

X, Y = map(int, input().split())

dst = math.sqrt(X*X + Y*Y)
dir = math.degrees(math.atan2(Y, X))

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

