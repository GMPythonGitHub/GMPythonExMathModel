## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_03c_geom_multiples:: //, function

A, B = map(int, input().split())

def multiples(A, B):
    AquoB, AsupB = A // B, A % B
    return (
        A // B * B, (A - 1) // B * B,
        (A + B - 1) // B * B, (A + B) // B * B )

ABle, ABlt, ABge, ABgt = multiples(A, B)
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

