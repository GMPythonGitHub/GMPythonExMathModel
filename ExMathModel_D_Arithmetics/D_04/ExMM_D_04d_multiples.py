## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_E_04d_vector::

A, B = map(int, input().split())

class Multiples():
    def __init__(self, a, b):
        self.a, self.b = a, b

    def able(self):
        return self.a // self.b * self.b
    def ablt(self):
        return (self.a - 1) // self.b * self.b
    def abge(self):
        return (self.a + self.b - 1) // self.b * self.b
    def abgt(self):
        return (self.a + self.b) // self.b * self.b
    def calc(self):
        return self.able(), self.ablt(), self.abge(), self.abgt()

ABle, ABlt, ABge, ABgt = Multiples(A, B)
print(f'{ABle = }, {ABlt = }, {ABge = }, {ABgt = }')

# =========================================================
# *** list of input lines ***
'''
A B

[Case a]
15 5 

[Case b]
16 5

[Case c]
14 5

'''

