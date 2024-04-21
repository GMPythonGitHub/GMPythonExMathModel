## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_04e_vector_product:: tuple, class

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))


class Vector():
    def __init__(self, xx=0, yy=0):
        self.set_xxyy(xx, yy)

    def set_xxyy(self, xx, yy):
        self.xx, self.yy = xx, yy

    def set_rrth(self, rr, th):
        self.rr, self.th = rr, math.radians(th)

    def xx(self):
        return self.xx

    def yy(self):
        return self.yy

    def xxyy(self):
        return self.xx, self.yy

    def rr(self):
        return math.sqrt(self.xx ** 2 + self.yy ** 2)

    def th(self):
        return math.degrees(math.atan2(self.xx, self.yy))

    def rrth(self):
        return self.rr(), self.th()
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

