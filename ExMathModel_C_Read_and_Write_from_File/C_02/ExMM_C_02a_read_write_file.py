## GMPython Exercises for Mathematical Modeling:: coded by Kinya MIURA
## ExMM_C_02a_read_write_file.py:: open(), write()

with open('sample_data_02.txt', 'r') as data_file:  # generator
    lst = []
    for i, line in enumerate(data_file):
        dlst = list((line.split()))  # removing '\n'
        lst.extend(dlst)

with open('sample_data_02_out.txt', 'w') as data_file:
    for i, lsti in enumerate(lst):
        if i % 5 == 5 - 1:
            data_file.write(lsti+'\n')  # write string to file
        else:
            data_file.write(lsti+' ')  # write string to file

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

