## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_02a_prime_factors::

N = int(input())

prmfac_list = []  # list of prime factors
nn, prmfac = N, 2
while nn > 1:
    if nn % prmfac == 0:
        prmfac_list.append(prmfac)
        nn //= prmfac
    else:
        prmfac += 1

print(f'{prmfac_list = }')

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

