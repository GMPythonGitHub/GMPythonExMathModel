## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06a_integer_matrix.py:: 2-D list, list comprehension,

H, W = map(int, input().split())

A = [[None] * W for _ in range(H)]  # 2-D list for matrix
for i in range(H):
    Ai = list(map(int, input().split()))
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
H W
A11 A12 ... A1W
A21 A22 ... A2W
...
AH1 AH2 ... AHW

[Case a]
6 6
0 1 2 3 4 5
5 0 1 2 3 4
4 5 0 1 2 3
3 4 5 0 1 2
2 3 4 5 0 1
1 2 3 4 5 0 

[Case b]
6 3
0 1 2
1 2 0
2 0 1
0 1 2
1 2 0
2 0 1

'''

