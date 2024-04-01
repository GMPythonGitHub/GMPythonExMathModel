## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_06a_list_calc.py:: extract

N = int(input())
A = list(map(int, input().split()))  # list

# absolute
Aa = [Ai for i, Ai in enumerate(A) if (i+1)%2 == 0]

Ab = [Ai for Ai in A if Ai%2 == 0]

print(f'{A = }\n{Aa = }\n{Ab = } ')

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
10
-4 -3 -2 -1 0 1 2 3 4 5

'''

