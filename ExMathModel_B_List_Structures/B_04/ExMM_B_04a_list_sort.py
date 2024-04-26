## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_04a_list_sort.py:: select sort

N = int(input())
A = list(map(int, input().split()))  # list

# select sort
sortAa = A.copy()
for i in range(N-1):  # ascending
    minA = i
    for j in range(i+1, N):
        if sortAa[minA] > sortAa[j]:
            minA = j
    sortAa[i], sortAa[minA] = sortAa[minA], sortAa[i]

sortAd = A.copy()
for i in range(N-1):  # descending
    maxA = i
    for j in range(i+1, N):
        if sortAd[maxA] < sortAd[j]:
            maxA = j
    sortAd[i], sortAd[maxA] = sortAd[maxA], sortAd[i]

print(f'{A = }')
print(f'{sortAa = }')
print(f'{sortAd = }')

# =========================================================
# *** list of input lines ***
'''
N
A1 A2 ... AN

[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
10
5 2 0 4 3 5 1 0 5 2

'''

