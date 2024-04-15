## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_02b_list_exchange.py:: slicing

N = int(input())
A = list(map(int, input().split()))  # list

B = A.copy()
for i in range(1, N, 2):
    B[i-1], B[i] = B[i], B[i-1]

print(f'{A = }\n{B = } ')

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

