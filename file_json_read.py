import json

file_in_path = 'data/simple_text.json'

with open(file_in_path, 'r') as f:
    f = json.load(f)
    emp_list = f['employees']
    for emps in emp_list:
        print(emps['firstName'], emps['lastName'])