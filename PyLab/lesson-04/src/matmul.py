import random
import time


def time_counter(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def time_counter_decorator(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Time cost of {func.__name__}: {end - start}s")
        return result

    return wrapper


# @time_counter_decorator
# def add(a, b, c):
#     return a + b + c

# def add(a, b, c):
#     return a + b + c
# add = time_counter_decorator(add)

# add(1,2,3)

# @time_counter_decorator
# def sub(a, b):
#     return b - a

# sub(2, 4)


def gen_random_list(n):
    # list: (n,)

    # result = []
    # for _ in range(n):
    #     result.append(random.randint(0, 99))
    # return result

    return [int(random.randint(0, 99)) for i in range(n)]


@time_counter_decorator
def mat_mul_v1(mat_1: list[list[float]], mat_2: list[list[float]]):
    result = []
    # mat_1 (m, k)
    # mat_2 (k, n)
    m = len(mat_1)
    k = len(mat_2)
    n = len(mat_2[0])

    # result (m, n)
    result = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            for x in range(k):
                result[i][j] += mat_1[i][x] * mat_2[x][j]

    return result


@time_counter_decorator
def mat_mul_v2(mat_1: list[list[float]], mat_2: list[list[float]]):
    result = []
    # mat_1 (m, k)
    # mat_2 (k, n)
    m = len(mat_1)
    k = len(mat_2)
    n = len(mat_2[0])

    # result (m, n)
    result = [[0 for _ in range(n)] for _ in range(m)]

    for i in range(m):
        for j in range(n):
            ks = [mat_1[i][x] * mat_2[x][j] for x in range(k)]
            result[i][j] = sum(ks)

    return result


@time_counter_decorator
def mat_add(mat_1, mat_2):
    pass


@time_counter_decorator
def mat_sub(mat_1, mat_2):
    pass


@time_counter_decorator
def mat_dot(mat_1, mat_2):
    pass


def is_odd(x: int):
    pass


def is_even(x: int):
    pass


def is_mat_same(mat_1, mat_2):
    if len(mat_1) != len(mat_2) or len(mat_1[0]) != len(mat_2[0]):
        return False

    # for i in range(len(mat_1)):
    #     for j in range(len(mat_1[0])):
    #         if mat_1[i][j] != mat_2[i][j]:
    #             return False

    # Shape: (len(mat_1)*len(mat_1[0]),)
    is_same = [
        mat_1[i][j] == mat_2[i][j]
        for i in range(len(mat_1))
        for j in range(len(mat_1[0]))
    ]
    return all(is_same)


def main():
    """
    (2, 3)
    1: []
    2: [[]]
    3: [[2, 3, ...]]
    3: [[2, 3, ...], []]
    4: [[2, 3, ...], [4, 5, ...]]
    ...

    [[0,3,4],
     [1,3,5]]
    """

    # # (m, k)
    # mat_1 = []
    # for i in range(m):
    #     mat_1.append([])
    #     for j in range(k):
    #         mat_1[i].append(random.randint(0, 99))

    # mat_1 = []  # (m, k)
    # for i in range(m):
    #     mat_1.append(gen_random_list(k))

    m = n = k = 500

    # (m, k)
    mat_1 = [gen_random_list(k) for _ in range(m)]
    # (k, n)
    mat_2 = [gen_random_list(n) for _ in range(k)]

    result_1 = mat_mul_v1(mat_1, mat_2)
    result_2 = mat_mul_v2(mat_1, mat_2)

    print(is_mat_same(result_1, result_2))


main()
