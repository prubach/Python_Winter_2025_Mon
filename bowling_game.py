"""
n  - number of rows

* * * * * *
 * * * * *
  * * * *
   * * *
    * *
     *

How many bowls do we need given n - the number of rows?

"""

def bowls_count(n):
    return


def bowls_sum_seq(n):
    return round(n*(n+1)/2)


def bowls_sum_loop(n):
    s = 0
    for i in range(n):
        s += i + 1
    return s


def bowls_sum_recursive(n):
    if n == 1:
        return 1
    else:
        return bowls_sum_recursive(n - 1) + n
    return s

if __name__ == '__main__':
    print(f'for n=5 using seq: {bowls_sum_seq(5)}')
    print(f'for n=6 using seq: {bowls_sum_seq(6)}')

    print(f'for n=5 using loop: {bowls_sum_loop(5)}')
    print(f'for n=6 using loop: {bowls_sum_loop(6)}')

    print(f'for n=5 using recursive: {bowls_sum_recursive(5)}')
    print(f'for n=6 using recursive: {bowls_sum_recursive(6)}')
