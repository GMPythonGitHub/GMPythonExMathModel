## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_00a_list_tuple_set.py:: list(), tuple(), set()

N = int(input())
S = input()  # string

strA = list(S.split())
lstA = []  # list of strings
for i in range(N):
    lstA.append(int(strA[i]))
print(f'{lstA = }')

tplA = tuple(lstA)
print(f'{tplA = }')

setA = set(lstA)
print(f'{setA = }')

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

