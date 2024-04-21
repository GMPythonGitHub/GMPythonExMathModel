## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_01a_divisors:: %, list

N = int(input())

A = []
for Ni in range(1, N+1):
    if N % Ni == 0:
        A.append(Ni)

print(len(A))
print(*A, sep=', ')

# =========================================================
# *** list of input lines ***
'''
N

[Case a]
360 

[Case b]
1

[Case c]
113

[Case d]
40320

'''

