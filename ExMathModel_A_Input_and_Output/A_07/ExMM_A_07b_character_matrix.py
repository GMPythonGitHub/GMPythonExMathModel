## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06b_character_matrix.py:: 2-D list, list comprehension, *list

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]  # 2-D list for matrix
T = []  # transformed
for i in range(W):
    Ti = []
    for j in range(H):
        Ti.append(S[j][i])
    T.append(Ti)

for Si in S:
    print(*Si, sep=', ')
print()

for Ti in T:
    print(*Ti, sep=', ')

# =========================================================
# *** list of input lines ***
'''
H W
S11 S12 ... S1W
S21 S22 ... S2W
...
SH1 SH2 ... SHW

[Case a]
6 6
######
#.xx.#
#x..x#
#.xx.#
#x..x#
######

[Case b]
6 3
###
#.#
#x#
#x#
#.#
###

'''

