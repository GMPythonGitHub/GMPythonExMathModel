## GMPython Exercises for Mathematical Modeling
## Ex_A_02_Integer_List_a.py:: input().split()

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    print(A[i], end=', ')
print()

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
6
100 130 110 140 150 120

'''

