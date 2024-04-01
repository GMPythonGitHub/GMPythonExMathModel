## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06b_character_mesh.py::

H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]
B = []  # transformed
for i in range(W):
    Bi = []
    for j in range(H):
        Bi.append(A[j][i])
    B.append(Bi)

for Ai in A:
    S = ''
    for Aij in Ai:
        S += Aij + ', '
    print(S)
print()

for Bi in B:
    S = ''
    for Bij in Bi:
        S += Bij + ', '
    print(S)

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

