## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_03b_geom_multiples:: %, //

A, B = map(int, input().split())

AquoB = A // B
AsupB = A % B

ABle = A // B * B
ABlt = (A - 1) // B * B
ABge = (A + B - 1) // B * B
ABgt = (A + B) // B * B

print(f'{ABle = }, {ABlt = }, {ABge = }, {ABgt = }')

# =========================================================
# *** list of input lines ***
'''
A B

[Case a]
15 5 

[Case b]
16 5

[Case c]
14 5

'''

