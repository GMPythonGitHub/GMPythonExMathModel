## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_01a_point_list:: sqrt()

import math

N = int(input())

XY = []
for _ in range(N):
    XY.append(tuple(map(int, input().split())))

distmax, distmin, distave = 0, float('inf'), 0
for i in range(0,N-1):
    xxi, yyi = XY[i]
    for j in range(i+1,N):
        xxj, yyj = XY[j]
        dist = math.sqrt((xxi-xxj)**2 + (yyi-yyj)**2)
        distmax = max(distmax, dist)
        distmin = min(distmin, dist)
        distave += dist
distave /= (N * (N-1) / 2)

print(f'{distmax = }, {distmin = }')
print(f'{distave = }')

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
5 4 
-4 3
-3 -4
4 -5

[Case b]
5
4 3
2 -5
-8 7
0 6
1 -9

'''

