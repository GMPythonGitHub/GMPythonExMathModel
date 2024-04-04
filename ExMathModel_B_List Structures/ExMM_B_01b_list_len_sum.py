## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_01b_list_len_sum.py:: len(), sum(), max(), min()

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
A1, A2, ...

[Case a]
8 4 9 5 3 6 0 2 7 1 

[Case b]
5 2 0 4 3 5 1 0 5 2

'''

