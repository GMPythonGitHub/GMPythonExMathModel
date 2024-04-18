## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_03a_geom_multiples:: %, //

A, B = map(int, input().split())

AquoB = A // B
AsupB = A % B

ABle = AquoB * B
ABlt = AquoB * B
if AsupB == 0:
    ABlt -= B
ABge = AquoB * B
if AsupB > 0:
    ABge += B
ABgt = AquoB * B + B

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

