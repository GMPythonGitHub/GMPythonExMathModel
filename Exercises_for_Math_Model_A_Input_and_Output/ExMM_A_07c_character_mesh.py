## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06c_character_mesh.py::

H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]
B = [[A[j][i] for j in range(H)] for i in range(W)]  # transformed

for Ai in A:
    print(*Ai, sep=', ')
print()

for Bi in B:
    print(*Bi, sep=', ')

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

