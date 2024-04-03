## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_01b_list_len_sum.py::

N = int(input())
A = list(map(int, input().split()))  # list

lenA = len(A)
sumA = sum(A)
maxA, minA = max(A), min(A)

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

