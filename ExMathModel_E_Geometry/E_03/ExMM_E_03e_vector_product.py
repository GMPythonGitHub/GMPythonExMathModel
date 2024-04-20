## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03e_vector_product:: tuple, class

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))

class Vector():
    def __init__(self, xx, yy):
        self.xx, self.yy = xx, yy

    def distance(self):
        return math.sqrt(self.xx*self.xx + self.yy*self.yy)
    def direction(self):
        return math.degrees(math.atan2(self.xx, self.yy))
    def prop(self):
        return self.distance(), self.direction()

    def prod_dot(self, vect):
        return self.xx * vect.xx + self.yy * vect.yy
    def prod_cross(self, vect):
        return self.xx * vect.yy - self.yy * vect.xx
    def product(self, vect):
        return self.prod_dot(vect), self.prod_cross(vect)

vectA = Vector(*A)
vectB = Vector(*B)
dot, cross = vectA.product(vectB)

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

