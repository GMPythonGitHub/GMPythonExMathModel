## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_05d_triangle_side_area:: dot product, cross product, class

import math

A = tuple(map(int, input().split()))
B = tuple(map(int, input().split()))
C = tuple(map(int, input().split()))

class Triangle():
    def __init__(self, aa, bb, cc):
        self.aa, self.bb, self.cc = aa, bb, cc

    def vect(self, pb, pa):
        pax, pay = pa; pbx, pby = pb
        return (pbx-pax, pby-pay)

    def dot_prod(self, va, vb):
        vax, vay = va; vbx, vby = vb
        return vax * vbx + vay * vby
    def cross_prod(self, va, vb):
        vax, vay = va; vbx, vby = vb
        return vax * vby - vay * vbx

    def dist(self, pa, pb):
        pax, pay = pa; pbx, pby = pb
        return math.sqrt((pbx-pax)**2 + (pby-pay)**2)
    def lngaa(self):
        return self.dist(self.bb, self.cc)
    def lngbb(self):
        return self.dist(self.cc, self.aa)
    def lngcc(self):
        return self.dist(self.aa, self.bb)
    def area(self):
        vab = self.vect(self.aa, self.bb)
        vac = self.vect(self.aa, self.cc)
        return abs(self.cross_prod(vab, vac) / 2)

triangle = Triangle(A, B, C)

Alng = triangle.lngaa()
Blng = triangle.lngbb()
Clng = triangle.lngcc()

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

