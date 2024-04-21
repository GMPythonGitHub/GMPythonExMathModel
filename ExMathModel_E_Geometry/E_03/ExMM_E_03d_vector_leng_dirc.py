## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_03d_vector:: sqrt(), atan2(), class

import math

L, D = map(int, input().split())

class Vector():
    def __init__(self, xx=0, yy=0):
        self.set_xxyy(xx, yy)

    def set_xxyy(self, xx, yy):
        self.xx, self.yy = xx, yy
    def set_rrth(self, rr, th):
        self.xx = rr * math.cos(math.radians(th))
        self.yy = rr * math.sin(math.radians(th))

    def xx(self):
        return self.xx
    def yy(self):
        return self.yy
    def xxyy(self):
        return self.xx, self.yy

    def rr(self):
        return math.sqrt(self.xx**2 + self.yy**2)
    def th(self):
        return math.degrees(math.atan2(self.xx, self.yy))
    def rrth(self):
        return self.rr(), self.th()

vector = Vector()
vector.set_rrth(L, D)
xx, yy = vector.xxyy()

print(f'{xx = }, {yy = }')

# =========================================================
# *** list of input lines ***
'''
L D

[Case a]
4 30 

[Case b]
4 150

[Case c]
12 -120

[Case d]
12 -45

'''

