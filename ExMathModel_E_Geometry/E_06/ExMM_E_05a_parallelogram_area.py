## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_05a_triangle_side_area:: Heron's Formula

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

Alng = math.sqrt((B[0]-C[0])**2 + (B[1]-C[1])**2)
Blng = math.sqrt((C[0]-A[0])**2 + (C[1]-A[1])**2)
Clng = math.sqrt((A[0]-B[0])**2 + (A[1]-B[1])**2)

ss = (Alng + Blng + Clng) / 2
area = math.sqrt(ss * (ss-Alng) * (ss- Blng) * (ss-Clng))

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

