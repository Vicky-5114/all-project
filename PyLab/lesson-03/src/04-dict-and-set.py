import time
import random
import argparse


def time_counter(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        return result, end - start

    return wrapper


def gen_random_list(n):
    result = []
    for i in range(n):
        result.append(random.randint(0, 99))
    return result


@time_counter
def union_with_dict(list1, list2):
    count_dict = {}

    for num in list1:
        count_dict[num] = True

    for num in list2:
        count_dict[num] = True

    union = list(count_dict.keys())
    return union


@time_counter
def intersection_with_dict(list1, list2):
    count_dict1 = {}
    count_dict2 = {}

    for num in list1:
        count_dict1[num] = True

    for num in list2:
        count_dict2[num] = True

    intersection = []

    for num in count_dict1:
        if num in count_dict2:
            intersection.append(num)

    return intersection


@time_counter
def union_with_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    union = list(set1 | set2)
    return union


@time_counter
def intersection_with_set(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = list(set1 & set2)
    return intersection


def test(n):
    list1 = gen_random_list(n)
    list2 = gen_random_list(n)

    union1, time_union1 = union_with_dict(list1, list2)
    intersection1, time_intersection1 = intersection_with_dict(list1, list2)
    union1.sort()
    intersection1.sort()

    union2, time_union2 = union_with_set(list1, list2)
    intersection2, time_intersection2 = intersection_with_set(list1, list2)
    union2.sort()
    intersection2.sort()

    print(union1 == union2, time_union1, time_union2)
    print(intersection1 == intersection2, time_intersection1, time_intersection2)


if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--n", type=int, help="number of data", default=int(1e6))
    args = arg_parser.parse_args()

    test(args.n)
