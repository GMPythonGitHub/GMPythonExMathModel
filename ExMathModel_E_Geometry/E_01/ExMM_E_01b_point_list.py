## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_01b_point_list:: sqrt(), list comprehension

import math

N = int(input())

XY = [tuple(map(int, input().split())) for _ in range(N)]

def distance(aa, bb):
    aax, aay = aa; bbx, bby = bb
    return math.sqrt((aax-bbx)**2 + (aay-bby)**2)

distmax, distmin, distave = 0, float('inf'), 0
for i in range(0,N-1):
    for j in range(i+1,N):
        dist = distance(XY[i], XY[j])
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

