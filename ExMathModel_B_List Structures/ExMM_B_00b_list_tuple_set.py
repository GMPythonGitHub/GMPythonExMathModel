## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_00b_list_tuple_sum.py:: map(), input().split(), list(), tuple(), set()

N = int(input())
lstA = list(map(int, input().split()))  # list
print(f'{lstA = } ')

tplA = tuple(lstA)  # tuple
print(f'{tplA = } ')

setA = set(lstA)  # set
print(f'{setA = } ')

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

