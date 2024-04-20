## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_01d_point_list:: sqrt(), atan2(), class

import math

N = int(input())

class Point():
    def __init__(self, xx, yy):
        self.xx, self.yy = xx, yy

    def dst(self):
        return math.sqrt(self.xx*self.xx + self.yy*self.yy)
    def dir(self):
        return math.degrees(math.atan2(self.yy, self.xx))
    def calc(self):
        return self.dst(), self.dir()

points = [Point(*map(int, input().split())) for _ in range(N)]

for point in points:
    dst, dir = point.calc()
    print(f'{dst = }, {dir = }')

# =========================================================
# *** list of input lines ***
'''
N
X1 Y1
X2 Y2
...
XN YN

[Case a]
4
3 4 
-4 3
-3 -4
4 -3

[Case b]
5
8 3
2 -5
-4 7
0 6
1 -9

'''

