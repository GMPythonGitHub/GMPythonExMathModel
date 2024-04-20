## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03d_vector_product:: tuple, class

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

class Vectors():
    def __init__(self, aa, bb):
        self.aa, self.bb = aa, bb  # instance variables; tuple

    def prod_dot(self):
        aax, aay = self.aa; bbx, bby = self.bb
        return aax * bbx + aay * bby
    def prod_cross(self):
        aax, aay = self.aa; bbx, bby = self.bb
        return aax * bby - aay * bbx
    def product(self):
        return self.prod_dot(), self.prod_cross()

vectors = Vectors(A, B)
dot, cross = vectors.product()

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

