## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_04b_string_list.py:: list comprehension

N = int(input())
A = [input() for _ in range(N)]

print(*A, sep=', ')

# =========================================================
# *** list of input lines ***
'''
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

