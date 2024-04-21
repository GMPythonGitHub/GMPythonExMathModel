## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_D_03b_gcd_lcm:: %, while-loop, mutual division method

A, B = map(int, input().split())

aa, bb = A, B
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
lcm = A * B // gcd

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

