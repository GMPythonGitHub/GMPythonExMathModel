## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_05a_geom_point_list:: sqrt(), atan2()

import math

N = int(input())

for _ in range(N):
    xx, yy = map(int, input().split())
    len = math.sqrt(xx*xx + yy*yy)
    dir  = math.degrees(math.atan2(yy, xx))
    print(f'{len = }, {dir = }')

# =========================================================
# *** list of input lines ***
'''
X Y

[Case a]
4
3 4 
-3 -4
-3 -4
3 -4

[Case b]
5
8 3
2 -5
-4 7
0 6
1 -9

'''

