def div(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    except:
        print("try中发生异常")


div(2, 1)
div(2, 0)
div("2", 2)


def div(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    except ZeroDivisionError:
        print("try中发生了除数为0的异常")
    except TypeError:
        print("try中发生了类型异常")


div(2, 1)
div(2, 0)
div("2", 2)


def div(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    except (ZeroDivisionError, TypeError):
        print("try中发生了除数为0的异常或者类型异常")


div(2, 1)
div(2, 0)
div("2", 2)


def div(a, b):
    try:
        try:
            c = a / b
            print(f"{a} / {b} = {c}")
        except ZeroDivisionError:
            print("try中发生了除数为0的异常")
    except:
        print("发生了除0以外的异常")


div("2", 2)


def div(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    finally:
        print("执行finally子句")


div(2, 0)


def div(a, b):
    try:
        c = a / b
        print(f"{a} / {b} = {c}")
    except:
        print("try中发生异常")
    finally:
        print("执行finally子句")


div(2, 0)


def return_num():
    try:
        return 1
    finally:
        return 2


print(return_num())
