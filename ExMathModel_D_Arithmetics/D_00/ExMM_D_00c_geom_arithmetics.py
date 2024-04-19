## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_00c_geom_arithmetics:: +, -, *, /: function

A, B = map(int, input().split())

def arithmetics(A, B):
    return A + B, A - B, A * B, A / B

add, sub, mul , div = arithmetics(A, B)
print(f'{add = }, {sub = }, {mul = }, {div = }')

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

