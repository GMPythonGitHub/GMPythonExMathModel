## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_03d_list_reverse.py:: list slicing

N = int(input())
A = list(map(int, input().split()))  # list

B = A[::-1]

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

