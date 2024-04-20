## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_02d_vector:: sqrt(), atan2(), class

import math

X, Y = map(int, input().split())

class Vector():
    def __init__(self, xx, yy):
        self.xx, self.yy = xx, yy

    def distance(self):
        return math.sqrt(self.xx*self.xx + self.yy*self.yy)
    def direction(self):
        return math.degrees(math.atan2(self.xx, self.yy))
    def prop(self):
        return self.distance(), self.direction()

vector = Vector(X, Y)
dst, dir = vector.prop()

print(f'{dst = }, {dir = }')

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

