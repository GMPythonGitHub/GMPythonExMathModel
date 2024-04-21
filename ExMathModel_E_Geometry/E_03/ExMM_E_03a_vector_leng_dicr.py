## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03a_vector:: sqrt(), atan2()

import math

L, D = map(int, input().split())

xx = L * math.cos(math.radians(D))
yy = L * math.sin(math.radians(D))

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

