## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_02a_prime_factors:: %, while-loop

N = int(input())

A = []  # list of prime factors
nn, prmfac = N, 2
while nn > 1:
    if nn % prmfac == 0:
        A.append(prmfac)
        nn //= prmfac
    else:
        prmfac += 1

print(f'{len(A) = }')
print(f'{A = }')

# =========================================================
# *** list of input lines ***
'''
N

[Case a]
60 

[Case b]
1

[Case c]
720

[Case d]
1212750

'''

