## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03a_vector_rrth:: sqrt(), atan2()

import math

R, T = map(int, input().split())

xx = R * math.cos(math.radians(T))
yy = R * math.sin(math.radians(T))

print(f'{xx = }, {yy = }')

# =========================================================
# *** list of input lines ***
'''
L D

[Case a]
4 30 

[Case b]
4 150

[Case c]
12 -120

[Case d]
12 -45

'''

