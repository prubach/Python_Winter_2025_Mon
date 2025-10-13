
if __name__ == '__main__':
    print('Hello')
    print('World')
    print('ABC')

    a = 1.79e308
    b = 10*a
    s = 'a={}, b={}'
    t = s.format(a, b)
    print(t)

    c = 4.94e-324
    d = c / 10

    print('c={}, d={}'.format(c, d))

    print('-----------')
    a1 = 454.6456
    print('a1={}'.format(a1))
    print(type(a1))

    a2 = round(a1)
    print('a2={}'.format(a2))
    print(type(a2))

    a3 = int(a1)
    print('a3={}'.format(a3))
    print(type(a3))

    a4 = '4545868'
    print('a4={}'.format(a4))
    print(type(a4))

    a5 = int(a4)
    print('a5={}'.format(a5))
    print(type(a5))


    b1 = 0b1001001
    print('b1={}'.format(b1))

    x1 = 0xf0
    print('x1={}'.format(x1))

    y1 = b1 + x1
    print('y1={}'.format(y1))
# else:
#     print('Hello')

