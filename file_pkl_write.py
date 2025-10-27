import pickle

file_out_path = 'data/simple_text.pkl'

emps = {"employees":[
  { "firstName":'John', "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":'Peter', "lastName":"Jones" }
]}

with open(file_out_path, 'wb') as f:
    f.write(pickle.dumps(emps))