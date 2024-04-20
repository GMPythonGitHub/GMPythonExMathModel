## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03c_vector_product:: tuple, function

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

def product(aa, bb):
    aax, aay = aa; bbx, bby = bb
    return (
        aax * bbx + aay * bby,
        aax * bby - aay * bbx )

dot, cross = product(A, B)

print(f'{dot = }, {cross = }')

# =========================================================
# *** list of input lines ***
'''
Ax Ay 
Bx By

[Case a]
3 4 
3 4 

[Case b]
3 4 
-4 3

[Case c]
3 4 
4 -3

[Case d]
3 4 
-3 -4

'''

