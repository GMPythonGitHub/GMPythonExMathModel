## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_A_03b_integer_list_b.py:: list comprehension, append()

N = int(input())
Astr = [input() for _ in range(N)]  # list strings: comprehension

Aint = []  # list of integers
for Astri in Astr:
    Aint.append(int(Astri))

S = ''  # string
for Ainti in Aint:
    S += str(Ainti) + ', '
print(S)

# =========================================================
# *** list of input lines ***
'''
[Case a]
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

[Case b]
6
100 
130 
110 
140 
150 
120

'''

