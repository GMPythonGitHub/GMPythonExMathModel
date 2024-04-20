## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_00d_arithmetics:: +, -, *, /: class

A, B = map(int, input().split())

class Arithmetics():
    def __init__(self, a, b):
        self.a, self.b = a, b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def calc(self):
        return self.add(), self.sub(), self.mul(), self.div()



AB = Arithmetics(A, B)
add, sub, mul , div = AB.calc()
print(f'{add = }, {sub = }, {mul = }, {div = }')

# =========================================================
# *** list of input lines ***
'''
A B

[Case a]
20 10 

[Case b]
20 -40

[Case c]
-80 40

[Case d]
-80 -160

'''

