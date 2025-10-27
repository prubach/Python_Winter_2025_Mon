import pickle

file_in_path = 'data/simple_text.pkl'

with open(file_in_path, 'rb') as f:
    f = pickle.load(f)
    emp_list = f['employees']
    for emps in emp_list:
        print(emps['firstName'], emps['lastName'])