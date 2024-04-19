## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_05a_list_calc.py:: absolute, square, list comprehension

N = int(input())
A = list(map(int, input().split()))  # list

# absolute
absA = [Ai if Ai >= 0 else -Ai for Ai in A]

sqrA = [Ai*Ai for Ai in A]

print(f'{A = }\n{absA = }\n{sqrA = } ')

# =========================================================
# *** list of input lines ***
'''
N
A1 A2 ... AN

[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
11
-5 -4 -3 -2 -1 0 1 2 3 4 5

'''

