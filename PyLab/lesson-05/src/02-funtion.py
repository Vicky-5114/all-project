from typing import Callable, Any


def foo_decorator(func: Callable[[Any], Any]):
    def wrapper(*args, **kwargs):
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        help(func)
        print(f"annotations: {func.__annotations__}")
        return func(*args, **kwargs)

    return wrapper


@foo_decorator
def foo(a: int, b: float, c: str, d: int = 0) -> str:
    """
    Foo function.

    Parameters
    ----------
    a: int
        An integer.
    b: float
        A float.
    c: str
        A str.
    """
    return str(a) + str(b) + str(c) + str(d)


def foo2(a, b, *args):
    return a + b


if __name__ == "__main__":
    print(foo_decorator.__annotations__)
    foo(1, 2, c="3")
    print(foo2(1, 2, 3, 4, 5))
    foo3 = lambda a, b, c, *args: a + b + c
    print(foo3(1, 2, 3, 4, 5))
