## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_01a_point_list:: sqrt(), atan2()

import math

N = int(input())

for _ in range(N):
    xx, yy = map(int, input().split())
    dst = math.sqrt(xx*xx + yy*yy)
    dir = math.degrees(math.atan2(yy, xx))
    print(f'{dst = }, {dir = }')

# =========================================================
# *** list of input lines ***
'''
N
X1 Y1
X2 Y2
...
XN YN

[Case a]
4
3 4 
-4 3
-3 -4
4 -3

[Case b]
5
4 3
2 -5
-8 7
0 6
1 -9

'''

