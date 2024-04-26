## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_00a_read_write_file.py:: open(), write()

with open('sample_data_00.txt', 'r') as data_file:  # generator
    lst = []
    for line in data_file:
        lst.append(line.strip())  # removing '\n'

with open('sample_data_00_out.txt', 'w') as data_file:
    for lsti in lst:
        data_file.write(lsti+'\n')  # write string to file

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

