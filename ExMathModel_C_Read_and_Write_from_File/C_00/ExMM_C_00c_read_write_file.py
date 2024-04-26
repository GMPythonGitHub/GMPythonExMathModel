## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_00c_read_write_file.py:: open(), readlines(), writelines()

with open('sample_data_00.txt', 'r') as data_file:  # generator
    lst = data_file.readlines()  # read all lines from file to list
    for i in range(len(lst)):
        lst[i] = lst[i].strip()

with open('sample_data_00_out.txt', 'w') as data_file:
    data_file.writelines(lst)  # write list to file

print(f'{lst = }')

# =========================================================
# *** list of input lines ***
'''
S1 S2 ... SN

[Case a]
10
0 1 2 3 4 5 6 7 8 9

[Case b]
9
-4 -3 -2 -1 0 1 2 3 4

'''

