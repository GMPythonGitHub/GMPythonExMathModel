## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_01c_divisors:: %, list, function

N = int(input())

def divisors(nn):
    divisorslst = []
    for nni in range(1, nn+1):
        if nni * nni > nn:
            break
        if nn % nni == 0:
            if nni * nni == nn:
                divisorslst.append(nni)
            else:
                divisorslst.append(nni)
                divisorslst.append(nn // nni)
    divisorslst.sort()
    return divisorslst

A = divisors(N)

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
40320

'''

