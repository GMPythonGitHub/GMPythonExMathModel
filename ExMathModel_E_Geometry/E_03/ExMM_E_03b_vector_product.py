## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03b_vector_product:: function

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

def prod_dot(aax, aay, bbx, bby):
    return aax * bbx + aay * bby

def prod_cross(aax, aay, bbx, bby):
    return aax * bby - aay * bbx

dot = prod_dot(Ax, Ay, Bx, By)
cross = prod_cross(Ax, Ay, Bx, By)

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

