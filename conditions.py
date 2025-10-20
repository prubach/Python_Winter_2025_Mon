p = False
q = False


# if p:
#     print('p')
#     a = 10
# else:
#     print('not p')
#     a = 8
#
# print(f'a={a}')
print('--------\n')
print(f'p={p}, q={q}')
print('--------')
if p and q:
    print('p and q')
else:
    print('not p and q')
print('--------')
if p or q:
    print('p or q')
else:
    print('not p or q')
print('--------')
if p and not q:
    print('p and not q')
else:
    print('not p or q')
print('--------')
if p ^ q:
    print('p xor q')
else:
    print('not p xor q')