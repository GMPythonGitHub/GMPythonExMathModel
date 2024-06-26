## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_03b_list_reverse.py::

N = int(input())
A = list(map(int, input().split()))  # list

B = [None] * N
for i, Ai in enumerate(A):
    B[N-i-1] = Ai

print(f'{A = }')
print(f'{B = }')

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

