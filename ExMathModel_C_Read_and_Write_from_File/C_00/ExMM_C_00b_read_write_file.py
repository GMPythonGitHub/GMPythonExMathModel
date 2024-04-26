## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_00b_read_write_file.py:: open(), readline(), write()

with open('sample_data_00.txt', 'r') as data_file:  # generator
    lst = []
    line = data_file.readline()  # read single line from file to string
    while line:
        lst.append(line.strip())  # removing '\n'
        line = data_file.readline()  # read single line from file to string

with open('sample_data_00_out.txt', 'w') as data_file:
    for ilst in lst:
        data_file.write(ilst+'\n')  # write string to file

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

