## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_01c_point_list:: sqrt(), list comprehension, list

import math

N = int(input())

XY = [tuple(map(int, input().split())) for _ in range(N)]

def distance(aa, bb):
    aax, aay = aa; bbx, bby = bb
    return math.sqrt((aax-bbx)**2 + (aay-bby)**2)

dist_lst = []
distave = 0
for i in range(0,N-1):
    for j in range(i+1,N):
        dist = distance(XY[i], XY[j])
        dist_lst.append([dist, (i+1,j+1)])
        distave += dist

print(f'{dist_lst = }')
dist_lst.sort()
print(f'{dist_lst = }')
distave /= (N * (N-1) / 2)

distmax, ijmax = dist_lst[-1]
distmin, ijmin = dist_lst[0]
print(f'{distmax = }, {ijmax = }')
print(f'{distmin = }, {ijmin = }')
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
4 -6

[Case b]
5
4 3
2 -5
-8 7
0 6
1 -9

'''

