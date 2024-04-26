## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_01b_read_write_file.py:: open(), readline(), write()

with open('sample_data_01.txt', 'r') as file_data:  # generator
    line = file_data.readline()  # read single line from file to string
    lst = list(line.split())

with open('sample_data_01_out.txt', 'w') as file_data:
    file_data.write(' '.join(lst))

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

