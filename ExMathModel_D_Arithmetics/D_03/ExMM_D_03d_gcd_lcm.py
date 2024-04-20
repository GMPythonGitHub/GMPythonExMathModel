## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_03c_gcd_lcm:: gcd(), lcm()

import math
math.factorial()

A, B = map(int, input().split())

gcd = math.gcd(A, B)
lcm = math.lcm(A, B)

print(f'{gcd = }, {lcm = }')

# =========================================================
# *** list of input lines ***
'''
A B

[Case a]
12 18 

[Case b]
36 12

[Case c]
25 36

[Case d]
1 12

'''

