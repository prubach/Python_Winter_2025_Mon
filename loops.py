for i in range(10):
    print(f'i={i}', end='\t')

print('\n----------')
for i in range(5, 10):
    print(f'i={i}', end='\t')

print('\n----------')
for i in reversed(range(5, 10)):
    print(f'i={i}', end='\t')

print('\n----------')
for i in reversed(range(5, 15, 2)):
    print(f'i={i}', end='\t')


print('\n----------')
ar1 = [ 131, 1542, 63645, 4635635 ]

for i in ar1:
    print(f'i={i}', end='\t')


print('\n----------')
s = 'dageheqwghqwehwghweqrhenłąąśżźżęęęb'

for i in s:
    print(f'i={i}', end='\t')

print('\n----------')
j = 1
while j < 6:
    #j = j + 1
    j += 1
    if j == 3:
        continue
    if j == 4:
        break
    print(f'j={j}', end='\t')

