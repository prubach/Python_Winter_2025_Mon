from time import time


def time_func(func, n):
    t0 = time()
    print(f'Running {func.__name__} with n={n}')
    res = func(n)
    print(f'Result={res}')
    t1 = time()
    elapsed = round(t1 - t0, 8)
    print(f'Done in {elapsed} sec')
