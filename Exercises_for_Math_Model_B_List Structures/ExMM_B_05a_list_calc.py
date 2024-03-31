## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_05a_list_calc.py:: abs(), **

N = int(input())
A = list(map(int, input().split()))  # list

# absolute
absA = []
for Ai in a:
    if Ai >= 0:
        absA.append(Ai)
    else:
        absA.append(-Ai)

sqrA = []
for Ai in A:
    sqrA.append(Ai**2)

print(f'{A = }\n{absA = }\n{sqrA = } ')

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
10
-4 -3 -2 -1 0 1 2 3 4 5

'''

