## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_02a_geom_gcm_lcm::

A, B = map(int, input().split())

for i in range(min(A,B), 0, -1):
    if A % i == 0 and B % i == 0:
        gcd = i
        break
lcm = A * B // gcd

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

