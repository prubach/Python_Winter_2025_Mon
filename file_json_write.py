import json

file_out_path = 'data/simple_text.json'

emps = {"employees":[
  { "firstName":'John', "lastName":"Doe" },
  { "firstName":"Anna", "lastName":"Smith" },
  { "firstName":'Peter', "lastName":"Jones" }
]}

with open(file_out_path, 'w') as f:
    json.dump(emps, f)