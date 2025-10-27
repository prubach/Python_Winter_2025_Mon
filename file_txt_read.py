file_path = r'C:\Users\prubac\PycharmProjects\Python_Winter_2025_Mon\data\simple_text.txt'
#file_path = 'data/simple_text.txt'

f = open(file_path, 'r')
i = 0
for line in f:
    i+=1
    print(f'{i}: {line}', end='')
f.close()


# with open(file_path, 'r') as f:
#     i = 0
#     for line in f:
#         i+=1
#         print(f'{i}: {line}')