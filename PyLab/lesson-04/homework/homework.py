import time
from argparse import ArgumentParser
import copy
import random


def gen_random_list(n):
    return [int(random.randint(0, 99)) for _ in range(n)]


def time_counter_decorator(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Time cost of {func.__name__}: {end - start}s")
        return result

    return wrapper


@time_counter_decorator
def mat_add(mat_1: list[list[float]], mat_2: list[list[float]]):
    m, n = len(mat_1), len(mat_1[0])
    return [[mat_1[i][j] + mat_2[i][j] for j in range(n)] for i in range(m)]


@time_counter_decorator
def mat_sub(mat_1, mat_2):
    m, n = len(mat_1), len(mat_1[0])
    return [[mat_1[i][j] - mat_2[i][j] for j in range(n)] for i in range(m)]


@time_counter_decorator
def mat_dot(mat_1, mat_2):
    m, n = len(mat_1), len(mat_1[0])
    return [[mat_1[i][j] * mat_2[i][j] for j in range(n)] for i in range(m)]


def is_odd(x: int):
    # 0 -> 000
    # 1 -> 001
    # 2 -> 010
    # 3 -> 011
    # 4 -> 100(x)
    # ------------
    # &    001(1)
    # ------------
    #      001
    return x & 1 == 1


def is_even(x: int):
    return x & 1 == 0


# x | 1
# 0 -> 000 | 001 -> 001
# 1 -> 001 | 001 -> 001
# 2 -> 010 | 001 -> 011
# 3 -> 011 | 001 -> 011
# 4 -> 100 | 001 -> 101

# x ^ 1
# 0 -> 000 | 001 -> 001
# 1 -> 001 | 001 -> 000
# 2 -> 010 | 001 -> 011
# 3 -> 011 | 001 -> 001
# 4 -> 100 | 001 -> 101
# *** x ^ x = 0


def test():
    m = n = 500
    mat_1 = [gen_random_list(n) for _ in range(m)]
    mat_2 = [gen_random_list(n) for _ in range(m)]

    mat_add(mat_1, mat_2)
    mat_sub(mat_1, mat_2)
    mat_dot(mat_1, mat_2)
    print(is_odd(10))
    print(is_even(10))


if __name__ == "__main__":
    test()
