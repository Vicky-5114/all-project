import builtins

print(dir(builtins))
print(dir())
print(dir(str))

import random, copy


def func1(arg1, arg2):
    num = 666
    print(num)
    print(locals())


def func2(arg1, arg2):
    num = 777
    print(num)
    print(locals())


num = 111
func1(222, 333)
func2(444, 555)
print(globals())
print(locals())

exp = "abs(-3)"
print(eval(exp))
obj = "print(abs(-3))"
exec(obj)
obj = """
a = -3
if a < 0:
    print(-a)
else:
    print(a)
"""
exec(obj)

a, b = 1, 2


def func():
    a = 3
    print(eval("a + b"))
    print(eval("a + b", {"a": 4, "b": 5}))
    print(eval("a + b", {"a": 6, "b": 7}, {"a": 8, "b": 9}))
    print(eval("a + b", {"a": 6, "b": 7}, {"a": 8, "c": 9}))


func()


def outer():
    def inner():
        # global a
        b = a + 1
        a = a + 1
        print(a, b)

    inner()


a = 1
outer()
