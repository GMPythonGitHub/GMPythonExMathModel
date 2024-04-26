## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_00d_read_write_file.py:: open()，read(), write()

with open('sample_data_00.txt', 'r') as data_file:  # generator
    str = data_file.read()  # read all lines from file to string

with open('sample_data_00_out.txt', 'w') as data_file:
    data_file.write(str)  # write string to file

lst = str.split()

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

