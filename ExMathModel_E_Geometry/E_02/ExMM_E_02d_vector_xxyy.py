## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02d_vector_xxyy:: sqrt(), atan2(), class

import math

X, Y = map(int, input().split())

class Vector():
    def __init__(self, xx, yy):
        self.xx, self.yy = xx, yy

    def rr(self):
        return math.sqrt(self.xx**2 + self.yy**2)
    def th(self):
        return math.degrees(math.atan2(self.xx, self.yy))
    def rrth(self):
        return self.rr(), self.th()

vector = Vector(X, Y)
rr, th = vector.rrth()

print(f'{rr = }, {th = }')

# =========================================================
# *** list of input lines ***
'''
X Y

[Case a]
3 4 

[Case b]
-4 3

[Case c]
-3 -4

[Case d]
4 -3

'''

