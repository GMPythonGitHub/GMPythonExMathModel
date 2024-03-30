## GMPython Exercises for Mathematical Modeling
## Ex_A_02_Integer_List_a.py:: split(), list()

N = int(input())
S = input()  # string
Astr = list(S.split())  # list of strings

Aint = [None] * N  # list of integers
for i in range(N):
    Aint[i] = int(Astr[i])

for i in range(N):
    print(Aint[i], end=', ')
print()

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
6
100 130 110 140 150 120

'''

