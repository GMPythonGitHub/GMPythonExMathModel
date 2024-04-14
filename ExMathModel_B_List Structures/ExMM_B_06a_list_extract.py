## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_06a_list_calc.py:: append()

N = int(input())
A = list(map(int, input().split()))  # list

# absolute
Aa = []
for i in range(N):
    if (i+1) % 2 == 0:
        Aa.append(A[i])

Ab = []
for i in range(N):
    if A[i] % 2 == 0:
        Ab.append(A[i])

print(f'{A = }\n{Aa = }\n{Ab = } ')

# =========================================================
# *** list of input lines ***
'''
N
A1, A2, ..., AN

[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
9
-4 -3 -2 -1 0 1 2 3 4

'''

