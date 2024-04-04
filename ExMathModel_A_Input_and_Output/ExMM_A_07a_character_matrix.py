## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06a_integer_matrix.py::

H, W = map(int, input().split())

A = [[None] * W for _ in range(H)]  # list for mesh
for i in range(H):
    Ai = list(input())
    for j in range(W):
        A[i][j] = Ai[j]

for Ai in A:
    for Aij in Ai:
        print(Aij, end=', ')
    print()
print()

for i in range(W):  # transformed
    for j in range(H):
        print(A[j][i], end=', ')
    print()

# =========================================================
# *** list of input lines ***
'''
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

