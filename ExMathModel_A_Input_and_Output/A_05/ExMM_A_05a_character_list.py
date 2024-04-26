## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_05a_character_list.py:: list()

S = input()  # string
lenS = len(S)
A = list(S)  # list of characters

for i in range(lenS):
    print(A[i], end=', ')

# =========================================================
# *** list of input lines ***
'''
S

[Case a]
abcdefghij

[Case b]
012345

'''

