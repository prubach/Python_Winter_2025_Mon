my_list = [('EUR', 4.4), ('USD', 1.2), ('GBP', 0.8), ('EUR', 4.0)]

print(my_list)

my_dict = dict(my_list)

print(my_dict)

my_val = [x[1] for x in my_list]
print(my_val)

print(f'sum={sum(my_val)}')
print(f'max={max(my_val)}')
print(f'min={min(my_val)}')

