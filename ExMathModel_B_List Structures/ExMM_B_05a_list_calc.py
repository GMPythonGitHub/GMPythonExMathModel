## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_05a_list_calc.py:: absolute, square

N = int(input())
A = list(map(int, input().split()))  # list

# absolute
absA = []
for Ai in A:
    if Ai >= 0:
        absA.append(Ai)
    else:
        absA.append(-Ai)

sqrA = []
for Ai in A:
    sqrA.append(Ai*Ai)

print(f'{A = }\n{absA = }\n{sqrA = } ')

# =========================================================
# *** list of input lines ***
'''
N
A1 A2 ... AN

[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

'''

