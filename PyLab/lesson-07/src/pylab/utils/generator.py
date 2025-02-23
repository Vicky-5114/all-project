from typing import Generator, Iterator


def func():
    print("The function body starts executing...")
    return 2
    print("The function body continues execution...")
    return 4
    print("ending...")


res = func()
print(res)


def gen():
    print("The function body starts executing...")
    yield 2
    print("The function body continues execution...")
    yield 4
    print("ending...")


"""
包含yield关键字的函数就是生成器函数, 调用生成器函数不会执行函数
体代码, 而是直接返回一个生成器对象, 调用__next__()方法才会开始执行函数
体代码 
"""
g = gen()  # 返回生成器对象
print(isinstance(g, Generator))  # True
print("__iter__" in dir(g) and "__next__" in dir(g))  # True: 生成器实现了迭代器协议
print(isinstance(g, Iterator))  # True: 生成器一定也是迭代 器

"""
生成器对象调用__next__()方法就会开始执行函数体代码, 遇到 yield 则把
后面的数据返回, 然后挂起函数的状态, 直到下一次调用__next__()方法, 再
从挂起的状态继续往后执行, __next__()方法如果没有可以返回的值, 会抛出
StopIteration异常, 直到函数体执行完毕, 函数才算结束 
"""
print(g.__next__())
print(g.__next__())

""" 从上一步挂起状态继续往后执行, 输出: ending...
此时__next__()没有可以返回的值, 抛出 StopIteration 异常
函数体执行完毕, 函数结束 
"""
# print(g.__next__())

g2 = gen()  # g迭代完毕, 再建一个生成器
"""
生成器也是迭代器, 所以和迭代器逻辑是一样的, for语句在执行时会
先调用__iter__()方法, 返回self, 然后每次循环时, self调用一次
__next__()方法, 因为调用了该方法, 函数体就会开始执行, 执行到
yield, 把后面的数据返回, 然后函数挂起, 当循环又调用__next__()
方法时, 则从函数挂起处继续执行函数体, 而当没有 yield 时, 即没
有返回数据时, __next__()方法将引发 StopIteration 异常, for语
句会捕获这个异常来 break 循环 
"""

for i in g2:
    print(i)

""" list()、tuple()、set()、sum()等也是基于类似原理 """
print(list(g2))
print(tuple(g2))
print(set(g2))
print(sum(g2))


# 列表推导式
list1 = [i for i in range(5)]
print(type(list1))  # <class 'list'>
print(sum(list1))  # 10
print(sum(list1))  # 10

# 生成器表达式
gt1 = (i for i in range(5))
print(type(gt1))  # <class 'generator'>

"""
这里gt1第二次sum结果为什么是0, 而上面的list1却不是?
因为同一个gt1生成器对象, 第一次sum已经迭代完了, 而sum默认从0开
始累加, 结果就为0
而每次sum(list1)都会通过list的__iter__()方法返回新的迭代器,
并不是同一个 
"""
print(sum(gt1))  # 10
print(sum(gt1))  # 0

""" 
生成器表达式如果立即被外层的函数使用, 可以省略圆括号,
而不用写成 sum((i for i in range(5))) 
"""
print(sum(i for i in range(5)))  # 10


str1 = "abc"
list1 = [1, 2, 3]
tup1 = (1, 2, 3)
dict1 = {"one": 1, "two": 2, "three": 3}
set1 = {1, 2, 3}
# str1、list1、tup1、dict1、set1 支持迭代协议
print(iter(str1))
print(iter(list1))
print(iter(tup1))
print(iter(dict1))
print(iter(set1))


class MyObject:
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass


# MyObject() 支持序列协议
print(iter(MyObject()))


class MyObject1:
    def __init__(self):
        self.num = 3

    def __call__(self):
        self.num += 1
        return self.num


"""
有第二个参数 sentinel = 7, 且 MyObject1() 是可调用对象, 则每
次迭代时调用 MyObject1()() 即调用 __call__方法, 当结果为 sentinel 时,
触发StopIteration, 被list捕获, 停止迭代 
"""
call_iter = iter(MyObject1(), 7)
print(call_iter)
print(list(call_iter))  # [4, 5, 6]


str_iterator = iter("abcd")
print(next(str_iterator))  # "a"
print(next(str_iterator))  # "b"
print(next(str_iterator))  # "c"
print(next(str_iterator))  # "d"
print(next(str_iterator, "ef"))  # 迭代耗尽, 返回 "ef"
print(next(str_iterator))  # 迭代耗尽, 触发 StopIteration
