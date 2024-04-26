## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_04c_string_list.py:: list comprehension

N = int(input())
A = [input() for _ in range(N)]

print(', '.join(A))

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

