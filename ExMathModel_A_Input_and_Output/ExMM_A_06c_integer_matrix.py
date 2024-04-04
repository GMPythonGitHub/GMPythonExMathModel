## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_06b_integer_matrix.py:: 2-D list, list comprehension, *list

H, W = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(H)]  # 2-D list for matrix
B = [[A[j][i] for j in range(H)] for i in range(W)]  # transformed

for Ai in A:
    print(*Ai, sep=', ')
print()

for Bi in B:
    print(*Bi, sep=', ')

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

