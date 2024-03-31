## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_B_04b_list_sort.py:: bubble sort

N = int(input())
A = list(map(int, input().split()))  # list

# bubble sort
sortAa = A.copy()
for i in range(N-1):  # ascending
    for j in range(N-i-1):
        if sortAa[j] > sortAa[j+1]:
            sortAa[j], sortAa[j+1] = sortAa[j+1], sortAa[j]

sortAd = A.copy()
for i in range(N - 1):  # descending
    for j in range(N - i - 1):
        if sortAd[j] < sortAd[j + 1]:
            sortAd[j], sortAd[j + 1] = sortAd[j + 1], sortAd[j]

print(f'{A = }\n{sortAa = }\n{sortAd = } ')

# =========================================================
# *** list of input lines ***
'''
[Case a]
10
8 4 9 5 3 6 0 2 7 1 

[Case b]
10
5 2 0 4 3 5 1 0 5 2

'''

