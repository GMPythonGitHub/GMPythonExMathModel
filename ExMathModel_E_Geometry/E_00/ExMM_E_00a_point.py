## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_00a_point:: sqrt()

import math

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

dist = math.sqrt((Ax-Bx)**2 + (Ay-By)**2)

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

