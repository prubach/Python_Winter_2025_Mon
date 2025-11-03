from time import time
from bowling_game import bowls_sum_loop, bowls_sum_recursive, bowls_sum_seq

def time_func(func, n):
    t0 = time()
    print(f'Running {func.__name__} with n={n}')
    res = func(n)
    print(f'Result={res}')
    t1 = time()
    elapsed = round(t1 - t0, 8)
    print(f'Done in {elapsed} sec')

#n = 998
n = 25000000
#time_func(bowls_sum_recursive, n)
time_func(bowls_sum_loop, n)
time_func(bowls_sum_seq, n)
