## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_02b_prime_factors:: function

N = int(input())

def prime_factors(nn):
    prmfaclst = []  # list of prime factors
    prmfac = 2
    while nn > 1:
        if nn % prmfac == 0:
            prmfaclst.append(prmfac)
            nn //= prmfac
        else:
            prmfac += 1
    return prmfaclst

prmfac_list = prime_factors(N)

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

