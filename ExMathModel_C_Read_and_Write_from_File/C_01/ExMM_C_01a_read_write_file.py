## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_01a_read_write_file.py:: open(), write()

with open('sample_data_01.txt', 'r') as data_file:  # generator
    lst = list(data_file)

with open('sample_data_01_out.txt', 'w') as data_file:
    for ilst in lst:
        data_file.write(ilst+' ')  # write string to file

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

