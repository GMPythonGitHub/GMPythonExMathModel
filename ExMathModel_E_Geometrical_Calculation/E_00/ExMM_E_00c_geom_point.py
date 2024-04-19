## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_04c_geom_point:: sqrt(), atan2(), class

import math

X, Y = map(int, input().split())

class Point():
    def __init__(self, xx, yy):
        self.xx, self.yy = xx, yy

    def dst(self):
        return math.sqrt(self.xx*self.xx + self.yy*self.yy)
    def dir(self):
        return math.degrees(math.atan2(self.yy, self.xx))
    def calc(self):
        return self.dst(), self.dir()

point = Point(X, Y)
dst, dir = point.calc()
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

