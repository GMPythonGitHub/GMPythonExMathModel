## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06b_integer_matrix.py:: 2-D list, list comprehension

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]  # 2-D list for matrix
B = []  # transformed
for i in range(W):
    Bi = []
    for j in range(H):
        Bi.append(A[j][i])
    B.append(Bi)

for Ai in A:
    S = ''
    for Aij in Ai:
        S += str(Aij) + ', '
    print(S)
print()

for Bi in B:
    S = ''
    for Bij in Bi:
        S += str(Bij) + ', '
    print(S)

# =========================================================
# *** list of input lines ***
'''
[Case a]  Copy the following sentences to 'execution window' !
6 6
0 1 2 3 4 5
5 0 1 2 3 4
4 5 0 1 2 3
3 4 5 0 1 2
2 3 4 5 0 1
1 2 3 4 5 0 

[Case b]  Copy the following sentences to 'execution window' !
6 3
0 1 2
1 2 0
2 0 1
0 1 2
1 2 0
2 0 1

'''

