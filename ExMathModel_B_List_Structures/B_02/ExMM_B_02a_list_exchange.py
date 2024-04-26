## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_02a_list_exchange.py:: append()

N = int(input())
A = list(map(int, input().split()))  # list

B = []
for i in range(1, N, 2):
    B.append(A[i])
    B.append(A[i-1])

print(f'{A = }\n{B = } ')
print(f'{B = }')

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

