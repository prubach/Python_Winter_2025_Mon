import os

#file_path = r'C:\Users\prubac\PycharmProjects\Python_Winter_2025_Mon\data\simple_text.txt'
file_path = 'data/simple_text.txt'

file_out_path = 'data/simple_text_out.txt'

print(os.getcwd())


with (open(file_path, 'r') as f):
    file_contents = f.read()
    # i = 0
    # for line in f:
    #     i+=1
    #     print(f'{i}: {line}')

print(file_contents)

with open(file_out_path, 'a') as f:
    f.write(file_contents)
    f.write('\n')
    f.write('New added line 1\n')
    f.write('New added line 2\n')