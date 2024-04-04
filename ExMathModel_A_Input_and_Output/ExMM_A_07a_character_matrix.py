## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06a_character_matrix.py:: 2-D list, list comprehension

H, W = map(int, input().split())

S = [[None] * W for _ in range(H)]  # 2-D list for matrix
for i in range(H):
    Si = list(input())
    for j in range(W):
        S[i][j] = Si[j]

for Si in S:
    for Sij in Si:
        print(Sij, end=', ')
    print()
print()

for i in range(W):  # transformed
    for j in range(H):
        print(S[j][i], end=', ')
    print()

# =========================================================
# *** list of input lines ***
'''
H W
S11 S12 ... S1W
S21 S22 ... S2W
...
SH1 SH2 ... SHW

[Case a]  Copy the following sentences to 'execution window' !
6 6
######
#.xx.#
#x..x#
#.xx.#
#x..x#
######

[Case b]  Copy the following sentences to 'execution window' !
6 3
###
#.#
#x#
#x#
#.#
###

'''

