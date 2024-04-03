## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_02c_integer_list_a.py:: map(), *list

N = int(input())
A = list(map(int, input().split()))  # list of integers

print(*A, sep=', ')

# =========================================================
# *** list of input lines ***
'''
N
A1 A2 ... AN

[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
6
100 130 110 140 150 120

'''

