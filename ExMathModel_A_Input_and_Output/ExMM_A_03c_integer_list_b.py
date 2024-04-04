## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_02c_integer_list_a.py:: list comprehension, *list

N = int(input())
A = [int(input()) for _ in range(N)]  # list of integers

print(*A, sep=', ')

# =========================================================
# *** list of input lines ***
'''
N
A1
A2
...
AN

[Case a]  Copy the following sentences to 'execution window' !
10
8
4
9
5
3
6
0
2
7
1 

[Case b]  Copy the following sentences to 'execution window' !
6
100
130
110
140
150
120

'''

