## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_05c_triangle_side_area:: dot product, cross product, function

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

def dot_prod(aa, bb):
    aax, aay = aa; bbx, bby = bb
    return aax * bbx + aay * bby

def cross_prod(aa, bb):
    aax, aay = aa; bbx, bby = bb
    return aax * bby - aay * bbx

AB = (B[0]-A[0], B[1]-A[1])
BC = (C[0]-B[0], C[1]-B[1])
CA = (A[0]-C[0], A[1]-C[1])

Alng = math.sqrt(dot_prod(BC,BC))
Blng = math.sqrt(dot_prod(CA,CA))
Clng = math.sqrt(dot_prod(AB,AB))

area = abs(cross_prod(AB, CA) / 2)

print(f'{Alng = }, {Blng = }, {Clng = }')
print(f'{area = }')

# =========================================================
# *** list of input lines ***
'''
Ax Ay 
Bx By
Cx Cy

[Case a]
0 0
3 4 
-4 3 

[Case b]
0 0
-3 -4
4 -3

[Case c]
-11 28
-28 7
19 30

[Case d]
-43 -22
7 -35
-35 12

'''

