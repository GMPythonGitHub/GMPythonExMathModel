## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_00b_geom_arithmetics:: +, -, *, /: function

A, B = map(int, input().split())

def add(A, B):
    return A + B
def sub(A, B):
    return A - B
def mul(A, B):
    return A * B
def div(A, B):
    return A / B

print(f'{add(A, B) = }, {sub(A, B) = }, {mul(A, B) = }, {div(A, B) = }')

# =========================================================
# *** list of input lines ***
'''
A B

[Case a]
20 10 

[Case b]
20 -40

[Case c]
-80 40

[Case d]
-80 -160

'''

