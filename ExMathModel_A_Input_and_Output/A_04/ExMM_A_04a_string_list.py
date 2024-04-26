## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_04a_string_list.py::

N = int(input())
A = [None] * N  # list of strings
for i in range(N):
    A[i] = input()

for i in range(N):
    print(A[i], end=', ')

# =========================================================
# *** list of input lines ***
'''
N
S1
S2
...
SN

[Case a]
10
alpha
bravo
charlie
delta
echo
foxtrot
golf
hotel
india
juliet

[Case b]
6
abc
acb
bac
bca
cab
cba

'''

