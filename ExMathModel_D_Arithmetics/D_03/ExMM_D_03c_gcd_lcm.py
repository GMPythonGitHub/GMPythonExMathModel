## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_03c_gcd_lcm:: mutual division method, function

A, B = map(int, input().split())

def gcd_lcm(aa, bb):
    lcm = aa * bb
    while True:
        if aa > bb > 0:
            aa %= bb
            if aa == 0:
                gcd = bb
                break
        elif bb > aa > 0:
            bb %= aa
            if bb == 0:
                gcd = aa
                break
        elif aa == bb > 0:
            gcd = aa
            break
        else:
            gcd = 0
            break
    lcm //= gcd
    return gcd, lcm

gcd, lcm = gcd_lcm(A, B)

print(f'{gcd = }, {lcm = }')

# =========================================================
# *** list of input lines ***
'''
A B

[Case a]
12 18 

[Case b]
36 12

[Case c]
25 36

[Case d]
1 12

'''

