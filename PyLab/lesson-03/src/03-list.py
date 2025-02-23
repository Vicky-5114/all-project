import random
import time
import argparse


def time_counter(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


def gen_random_list(n):
    result = []
    for i in range(n):
        result.append(random.randint(0, 99))
    return result


def sum_list_v1(l: list):
    result = 0
    for e in l:
        result += e
    return result


def sum_list_v2(l: list):
    result = 0
    for i in range(len(l)):
        result += l[i]
    return result


# S(l, i) = l[i] + S(l, i-1)
def sum_list_v3(l: list, i: int):
    # Avoid too deep recursion
    if len(l) - i > 500:
        print("[WARNING] Too deep recursion! Current depth is", len(l) - i)
        return sum_list_v2(l[: i + 1])
    if i <= 0:
        return l[i]
    return l[i] + sum_list_v3(l, i - 1)


def union_brute_force(list1, list2):
    union = []
    for item in list1:
        if item not in union:
            union.append(item)
    for item in list2:
        if item not in union:
            union.append(item)
    return union


def intersection_brute_force(list1, list2):
    intersection = []
    for item in list1:
        if item in list2 and item not in intersection:
            intersection.append(item)
    return intersection


def union_marker(list1, list2):
    result = []
    marker = [0] * 100
    for item in list1:
        marker[item] = 1
    for item in list2:
        if marker[item] == 0:
            result.append(item)
            marker[item] = 1
    return result


def intersection_marker(list1, list2):
    result = []
    # Given that the values are integers between 0 and 99
    # Create a list of 100 elements, all set to 0
    marker = [0] * 100
    # Or: counter = [0 for _ in range(100)]
    for item in list1:
        marker[item] = 1
    for item in list2:
        if marker[item] == 1:
            result.append(item)
            marker[item] = 0
    return result


def test_sum_list(n: int):
    l = gen_random_list(n)
    print(time_counter(sum_list_v1, l))
    print(time_counter(sum_list_v2, l))
    print(time_counter(sum_list_v3, l, len(l) - 1))


def test_union(n: int):
    list1 = gen_random_list(n)
    list2 = gen_random_list(n)
    result1, time_cost1 = time_counter(union_brute_force, list1, list2)
    result2, time_cost2 = time_counter(union_marker, list1, list2)
    result1.sort()
    result2.sort()
    print(result1 == result2, time_cost1, time_cost2)


def test_intersection(n: int):
    list1 = gen_random_list(n)
    list2 = gen_random_list(n)
    result1, time_cost1 = time_counter(intersection_brute_force, list1, list2)
    result2, time_cost2 = time_counter(intersection_marker, list1, list2)
    result1.sort()
    result2.sort()
    print(result1 == result2, time_cost1, time_cost2)


def main(args):
    test_sum_list(args.n_sum)
    test_union(args.n_union)
    test_intersection(args.n_intersection)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "--n_sum",
        type=int,
        help="number of elements in the list for sum",
        default=int(1e5),
    )
    arg_parser.add_argument(
        "--n_union",
        type=int,
        help="number of elements in the list for union",
        default=int(1e5),
    )
    arg_parser.add_argument(
        "--n_intersection",
        type=int,
        help="number of elements in the list for intersection",
        default=int(1e5),
    )
    args = arg_parser.parse_args()
    main(args)
