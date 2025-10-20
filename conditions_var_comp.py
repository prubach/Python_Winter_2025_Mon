a = 22
b = 20

if a >= b:
    print('a >= b')
else:
    print('a < b')


s1 = 'abc'
s2 = str('abcd')

if s1 == s2:
    print('s1 == s2')

a = 10 if s1==s2 else 20
print(a)


s1 = 'abcsfgsg'

match s1:
    case 'a':
        print('s1 = a')
    case 'abc':
        print('s1 = abc')
    case 'abcd':
        print('s1 = abcd')
    case _:
        print('s1 not matched')

