import copy


def print_address(x, name):
    print(f"The address of {name} is: {hex(id(x))}")


def test_1():
    x = 999
    y = 999

    print(
        "The reason why x and y have the same address is that Python caches small integers."
    )
    print_address(x, "x_int")
    print_address(y, "y_int")

    x = "999"
    y = "999"

    print("Same string literals will have the same address too.")
    print_address(x, "x_str")
    print_address(y, "y_str")

    del x

    # print(x)
    print(y)
    print_address(y, "y")


def test_2():
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a
    # a and b have different addresses
    print_address(a, "a")
    print_address(b, "b")
    print_address(c, "c")
    a.append(4)
    print(a)
    print(c)
    print(b)


def shallow_copy_list():
    # List is mutable
    # Copying a list will create a new list with the same elements
    a = [1, 2, 3, []]
    b = copy.copy(a)

    # Not same, the list itself is copied, where each element
    # is a reference
    print_address(a, "a")
    print_address(b, "b")

    # Same, reference to the same object
    print_address(a[0], "a[0]")
    print_address(b[0], "b[0]")

    # Same, reference to the same list
    print_address(a[-1], "a[-1]")
    print_address(b[-1], "b[-1]")

    # Since the refence is to the same list, append happens to both
    # a and b
    a[-1].append(4)
    print(a)
    print(b)

    # a and b are different lists, changing the elements inside will
    # only affect a
    a.append(4)
    a[0] = 999
    print(a)
    print(b)
    print_address(a[0], "a[0]")
    print_address(b[0], "b[0]")


def shallow_copy_tuple():
    # Tuple is immutable
    # Copying a tuple is just copying the reference
    tup3 = (991, "abc", [])
    tup4 = copy.copy(tup3)
    # Same
    print_address(tup3, "tup3")
    print_address(tup4, "tup4")
    # Same
    print_address(tup3[-1], "tup3[-1]")
    print_address(tup4[-1], "tup4[-1]")


def deep_copy_list():
    # List is mutable
    # Deep copy will create a new list with new elements
    a = [1, 2, 3, []]
    b = copy.deepcopy(a)

    print_address(a, "a")
    print_address(b, "b")

    # Same
    print_address(a[0], "a[0]")
    print_address(b[0], "b[0]")

    # Not same
    print_address(a[-1], "a[-1]")
    print_address(b[-1], "b[-1]")

    # Since the refence is to the same list, append happens to both
    # a and b
    a[-1].append(4)
    print(a)
    print(b)

    # a and b are different lists, changing the elements inside will
    # only affect a
    a.append(4)
    a[0] = 999
    print(a)
    print(b)
    print_address(a[0], "a[0]")
    print_address(b[0], "b[0]")


def deep_copy_tuple():
    # Tuple is immutable
    # Deep copy will create a new tuple with new elements
    tup3 = (991, "abc", [])
    tup4 = copy.deepcopy(tup3)
    # Same
    print_address(tup3, "tup3")
    print_address(tup4, "tup4")
    # Not same
    print_address(tup3[-1], "tup3[-1]")
    print_address(tup4[-1], "tup4[-1]")


if __name__ == "__main__":
    # test_1()
    # test_2()
    # shallow_copy_list()
    # deep_copy_list()
    a = b = c = [1, 2, 3]
    b.append(4)
    print(a, b, c)
