import random
import timeit
# import pandas as pd

x = random.randint(10**3, 10**6)


def test_naive():
    a, b, c = x, 2 * x, x // 2


def test_shift():
    a, b, c = x, x << 1, x >> 1


def test_mixed():
    a, b, c = x, 2 * x, x >> 1


def test_mixed_swapped():
    a, b, c = x, x << 1, x // 2


def observe(k):
    print(k)
    print({
        'naive': timeit.timeit(test_naive),
        # 'shift': timeit.timeit(test_shift),
        # 'mixed': timeit.timeit(test_mixed),
        'mixed_swapped': timeit.timeit(test_mixed_swapped),
    })


if __name__ == "__main__":
    for k in range(100):
        observe(k)

