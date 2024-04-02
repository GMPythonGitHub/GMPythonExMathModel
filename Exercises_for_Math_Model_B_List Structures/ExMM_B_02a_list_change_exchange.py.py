## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_02a_list_len_sum.py::

N = int(input())
A = list(map(int, input().split()))  # list

# absolute
B = A.copy()
lenB = len(B)
for i in range(1, lenB, 2):
    B[i-1], B[i] = B[i], B[i-1]

print(f'{A = }\n{B = } ')

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

'''

