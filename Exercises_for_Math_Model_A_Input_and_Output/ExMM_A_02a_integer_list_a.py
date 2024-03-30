## GMPython Exercises for Mathematical Modeling
## ExMM_A_02a_integer_list_a.py:: input().split(), append()

N = int(input())
Astr = list(input().split())  # list of strings

Aint = []  # list of integers
for Astri in Astr:
    Aint.append(int(Astri))

S = ''  # string
for Ainti in Aint:
    S += str(Ainti) + ', '
print(S)

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

