## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_02a_geom_divisors::

N = int(input())

A = []
for Ni in range(1, N+1):
    if Ni * Ni > N:
        break
    if N % Ni == 0:
        if Ni * Ni == N:
            A.append(Ni)
        else:
            A.append(Ni)
            A.append(N // Ni)

A.sort()
print(len(A))
print(*A, sep=', ')

# =========================================================
# *** list of input lines ***
'''
N

[Case a]
3600

[Case b]
1

[Case c]
113

[Case d]
3628800
'''

