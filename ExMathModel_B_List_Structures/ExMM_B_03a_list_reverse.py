## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_03a_list_reverse.py:: append()

N = int(input())
A = list(map(int, input().split()))  # list

B = []
for i in range(N):
    B.append(A[N-1-i])

print(f'{A = }\n{B = } ')

# =========================================================
# *** list of input lines ***
'''
N
A1 A2 ... AN

[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
10
5 2 0 4 3 5 1 0 5 2

'''
