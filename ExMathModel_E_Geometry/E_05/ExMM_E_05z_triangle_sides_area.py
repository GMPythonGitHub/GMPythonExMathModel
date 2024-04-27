## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_05e_triangle_side_area:: dot product, cross product, class

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

class Triangle():
    def __init__(self, aa, bb, cc):
        self.aa, self.bb, self.cc = aa, bb, cc

    def vect(self, p2p):
        print(p2p)
        pa, pb = None, None
        if p2p == 'a2b': pa, pb = self.bb, self.aa
        elif p2p == 'b2a': pa, pb = self.aa, self.bb
        elif p2p == 'b2c': pa, pb = self.cc, self.bb
        elif p2p == 'c2b': pa, pb = self.bb, self.cc
        elif p2p == 'c2a': pa, pb = self.aa, self.cc
        elif p2p == 'a2c': pa, pb = self.cc, self.aa
        pax, pay = pa; pbx, pby = pb
        return (pbx-pax, pby-pay)

    def dot_prod(self, vap2p, vbp2p):
        va, vb = self.vect(vap2p), self.vect(vbp2p)
        vax, vay = va; vbx, vby = vb
        return vax * vbx + vay * vby
    def cross_prod(self, ap2p, bp2p):
        va, vb = self.vect(ap2p), self.vect(bp2p)
        vax, vay = va; vbx, vby = vb
        return vax * vby - vay * vbx

    def leng(self, p2p):
        return math.sqrt(self.dot_prod(p2p, p2p))
    def area(self):
        return abs(self.cross_prod('a2b', 'a2c') / 2)

triangle = Triangle(A, B, C)

Alng = triangle.leng('b2c')
Blng = triangle.leng('c2a')
Clng = triangle.leng('a2b')

area = triangle.area()

print(f'{Alng = }, {Blng = }, {Clng = }')
print(f'{area = }')

# =========================================================
# *** list of input lines ***
'''
Ax Ay 
Bx By
Cx Cy

[Case a]
0 0
3 4 
-4 3 

[Case b]
0 0
-3 -4
4 -3

[Case c]
-11 28
-28 7
19 30

[Case d]
-43 -22
7 -35
-35 12

'''

