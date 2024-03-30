## GMPython Exercises for Mathematical Modeling
## Ex_A: Input and Output
## Ex_A_00a.py:: using f-string

A = int(input())
B = float(input())
C = input()

# output with f-string
print(f'{A = }')  # with notation
print(f'{B = }')
print(f'{C = }')
print()

print(f'{A:d}')  # with index
print(f'{B:f}')
print(f'{C:s}')
print()

print(f'{A:05d}')  # with digit specification
print(f'{A:,d}')
print(f'{B:.4f}')
print(f'{B:.3e}')
print(f'{C:*<10}')  # with alignment
print(f'{C:*^10}')
print(f'{C:*>10}')

# =========================================================
# *** list of input lines ***
'''
[Case a]
12345
123.45
abcde

[Case B]
1234500000
0.00012345
abc de

'''


