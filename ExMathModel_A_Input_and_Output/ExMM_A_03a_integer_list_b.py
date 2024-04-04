## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_03a_integer_list_b.py::

N = int(input())
Astr = [None] * N  # list of strings
for i in range(N):
    Astr[i] = input()

Aint = [None] * N  # list of integers
for i in range(N):
    Aint[i] = int(Astr[i])

for i in range(N):
    print(Aint[i], end=', ')
print()

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

