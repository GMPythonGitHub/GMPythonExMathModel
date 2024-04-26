## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06c_character_matrix.py:: 2-D list, list comprehension, join()

H, W = map(int, input().split())

S = [list(input()) for _ in range(H)]  # 2-D list for matrix
T = [[S[j][i] for j in range(H)] for i in range(W)]  # transformed

for Si in S:
    print(', '.join(Si))
print()

for Ti in T:
    print(', '.join(Ti))

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

