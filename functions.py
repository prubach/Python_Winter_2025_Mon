
def sum_it(a, b):
    r = a + b
    c = 10
    return r

print(sum_it(1, 2))
#print(f'c={c}')


def sum_and_multiply_it(a, b):
    r1 = a + b
    r2 = a * b
    return r1, r2

a = 10
b = 20

ab_sum, ab_multiply = sum_and_multiply_it(a, b)
print(ab_sum)
print(ab_multiply)

print('-----------------')
t1 = sum_and_multiply_it(a, b)
print(t1)
print(t1[0])
print(t1[1])
# t1[1] = 100 - not possible - can't assign values to tuple
print(t1[1])

print('-----------------')
t2 = (1, 5, 6) # - tuple
l1 = [10, 50, 60] # - list
print(t2)
print(l1)
print('-----------')
l1[1] = 100
print(l1)
print('-----------')
l1.insert(1, 80)
l1.append(80)
print(f'l1={l1}')

set1 = set(l1)
print('set1={}'.format(set1))
print(f'sorted set1={sorted(set1)}')


l1.append(90)
print(l1)
l1.remove(80)
print(l1)
print('-------------')
l1.pop(0)
print(l1)

print('-------------')
l2 = list(t2)
print(l2)
l2.append(90)
print(l2)

