## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_04a_vector_product::

Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())

dot = Ax * Bx + Ay * By
cross = Ax * By - Ay * Bx

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

