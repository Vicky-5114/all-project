from typing import Iterable, Iterator

num1 = 123
str1 = "abc"
list1 = [1, 2, 3]
tup1 = (1, 2, 3)
dict1 = {"one": 1, "two": 2, "three": 3}
set1 = {1, 2, 3}
range1 = range(4)

print("__iter__" in dir(num1) or "__getitem__" in dir(num1))  # False
print("__iter__" in dir(str1))
print("__iter__" in dir(list1))
print("__iter__" in dir(tup1))
print("__iter__" in dir(dict1))
print("__iter__" in dir(set1))
print("__iter__" in dir(range1))


class MyObject1:
    def __init__(self):
        pass


mo1 = MyObject1()
print(isinstance(mo1, Iterable))  # False: 既不支持迭代协议, 也不支持序列协议


class MyObject2:
    def __init__(self):
        pass

    def __iter__(self):
        pass


mo2 = MyObject2()
print(isinstance(mo2, Iterable))  # True: 因为有__iter__() 方法, 即支持迭代协议


class MyObject3:
    def __init__(self):
        pass

    def __getitem__(self, index):
        pass


mo3 = MyObject3()
print(isinstance(mo3, Iterable))  # False


reversed1 = reversed([1, 3, 1, 4])
zip1 = zip([1, 2, 3], ["one", "two", "three"])
enumerate1 = enumerate([1, 2, 3])
print("__iter__" in dir(reversed1) and "__next__" in dir(reversed1))
print("__iter__" in dir(zip1) and "__next__" in dir(zip1))
print("__iter__" in dir(enumerate1) and "__next__" in dir(enumerate1))

print(next(zip1))
print(next(zip1))
print(next(zip1))


class MyObject1:
    def __init__(self):
        pass


mo1 = MyObject1()
print(isinstance(mo1, Iterator))  # False: 不支持迭代器协议


class MyObject2:
    def __init__(self):
        pass

    def __iter__(self):
        pass


mo2 = MyObject2()
print(isinstance(mo2, Iterator))  # False: 不支持迭代器协议


class MyObject3:
    def __init__(self):
        pass

    def __iter__(self):
        pass

    def __next__(self):
        pass


mo3 = MyObject3()
print(isinstance(mo3, Iterator))  # True: 支持迭代器协议


class ContainerIterator:
    def __init__(self, container):
        self.container = container
        self.cursor = 0

    def __iter__(self):  # 对应第 ② 点
        return self

    def __next__(self):  # 对应第 ③ 点
        if self.cursor < len(self.container.iterable):
            item = self.container.iterable[self.cursor]
            self.cursor += 1
            return item
        raise StopIteration


class Container:
    def __init__(self, iterable):
        self.iterable = iterable

    def __iter__(self):  # 对应第 ① 点
        return ContainerIterator(self)


cont = Container([4, 5, 6])


"""
for语句在执行时会先调用可迭代对象的__iter__()方法, 得到该方法返
回的迭代器对象,
然后每循环一次, 该迭代器对象调用一次__next__()方法, 通过
__next__()方法来逐一返回元素,
当元素用尽时, __next__()方法将抛出StopIteration异常, 而for语
句会捕获这个异常来break循环
"""
for item in cont:
    print(item)


""" for循环原理实现 """
cont_iterator = cont.__iter__()
while True:
    try:
        item = cont_iterator.__next__()
        print(item)
    except StopIteration:
        break

"""
除了for循环以外, 其他能够接收iterable参数的函数或方法大多都是基
于类似原理,
比如: list()、tuple()、set()、sum()等等 """
print(list(cont))
print(tuple(cont))
print(set(cont))
print(sum(cont))


"""
迭代器也是可迭代对象, for语句在执行时会先调用迭代器的__iter__()
方法,
而迭代器的__iter__()方法正好返回迭代器对象本身, 后面过程就是一
样的了"""
cont_iterator = cont.__iter__()
for k in cont_iterator:
    print(k)


"""
同一个迭代器只能往前不会后退, 这里print(j)不会出结果, 是因为for
语句遍历的
迭代器对象是cont_iterator, 在上文中该迭代器的self.cursor属性
已经到了最大,
这里继续对同一个迭代器进行遍历, 执行__next__()方法将直接抛出异
常, 结束循环 """
for j in cont_iterator:
    print(j)  # 没有输出

print(cont_iterator.__next__())  # 抛出 StopIteration 异常


class Container:
    def __init__(self, iterable):
        self.iterable = iterable

    def __getitem__(self, index):
        return self.iterable[index]


cont = Container([5, 6, 7])

"""
for语句在执行时, 先找__iter__()方法, 没有找到, 则找
__getitem__()方法, 然后
每循环一次, 调用一次__getitem__()方法, 其中index参数从0开始,
无限递增+1, 当
index超出iterable索引范围抛出IndexError, for语句会捕获这个异
常来break循环 
"""
for i in cont:
    print(i)

""" list()、tuple()、set()、sum()等也是基于类似原理 """
print(list(cont))
print(tuple(cont))
print(set(cont))
print(sum(cont))


""" 测试__getitem__()方法中的index参数 """


class MyObject:
    def __init__(self):
        pass

    def __getitem__(self, index):
        if index > 3:
            raise IndexError
        return index


mo = MyObject()
for i in mo:
    print(i)
print(list(mo))
print(tuple(mo))
print(set(mo))
