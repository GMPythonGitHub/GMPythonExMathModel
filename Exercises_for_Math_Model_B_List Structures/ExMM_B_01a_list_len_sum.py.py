## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_01a_list_len_sum.py::

N = int(input())
A = list(map(int, input().split()))  # list

lenA = 0
sumA = 0
maxA, minA = A[0], A[0]
for Ai in A:
    lenA += 1
    sumA += Ai
    if Ai > maxA:
        maxA = Ai
    if Ai < minA:
        minA = Ai

print(f'{A = } ')
print(f'{lenA = }, {sumA = }')
print(f'{maxA = }, {minA = }')

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
10
5 2 0 4 3 5 1 0 5 2

'''

