from numbers import Number


def byte_taken(object) -> int:
    return object.__sizeof__()


def print_number_info(number: Number):
    print(f"Number: {number}\tType: {type(number)}\nByte taken: {byte_taken(number)}")
    if not isinstance(number, Number):
        # raise TypeError("number must be a number type")
        print("The input param is not a Number!")


def test_int():
    a = int()
    print_number_info(a)
    b = 1
    print_number_info(b)
    c = int("2")
    print_number_info(c)
    d: int = 3.0
    print_number_info(d)
    e = int("101010", base=2)
    print_number_info(e)
    f = int("fffffffffabced", base=16)
    print_number_info(f)


def test_float():
    a = float()
    print_number_info(a)
    b = 1.0
    print_number_info(b)
    c = float("2.0")
    print_number_info(c)
    d = float("3e-2")
    print_number_info(d)


def test_bool():
    # fmt: off
    test_data = list([
        bool(), True, False, bool(1), bool(0), bool(1.0), bool(0.0), 
        bool("True"), bool("False"), bool("true"), bool("false"), bool("1"), 
        bool("0"), bool(""), bool(None), bool([]),
    ])
    # fmt: on
    for data in test_data:
        print_number_info(data)


def test_complex():
    # fmt: off
    test_data = list([
        complex(), complex(1), complex(1, 2), complex(1.0, 2.0), complex("1+2j"),
    ])
    # fmt: on

    # The reason why `list` is needed is that when using `map`, the map from func
    # to data is created but not executed. When adding a `list`, i.e., creating a
    # list from the map by iterating over the map, the map is executed.
    list(map(print_number_info, test_data))


def main():
    # test_int()
    test_bool()


if __name__ == "__main__":
    main()
