## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_05c_geom_point_list:: sqrt(), atan2(), list, list comprehension

import math

N = int(input())
XY = [tuple(map(int, input().split())) for _ in range(N)]

def point(xx, yy):
    return (
        math.sqrt(xx*xx + yy*yy),
        math.degrees(math.atan2(yy, xx)) )

for XYi in XY:
    dst, dir = point(*XYi)
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
8 3
2 -5
-4 7
0 6
1 -9

'''

