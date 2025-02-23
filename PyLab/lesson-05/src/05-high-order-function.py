object1 = filter(lambda x: x - 1, [1, 2, 3, False, 4])
print(list(object1))
object2 = filter(lambda x: print(x - 1), [1, 2, 3, False, 4])
print(list(object2))
object3 = filter(None, [1, 2, 0, 3, False, 4])
print(list(object3))


def square(a):
    return a**2


result = map(square, [1, 2, 3])
print(list(result))
result = map(lambda a: a**2, [1, 2, 3])
print(list(result))
result = list(map(float, ["1", "2", "3"]))
print(result)

result = list(map(lambda x, y, z: x + y + z, [1, 2, 3], [3, 2, 1], [1, 3, 2]))
print(result)
result = list(map(lambda x, y, z: x + y + z, [1, 2, 3], [3, 2, 1], [1, 3]))
print(result)


from functools import reduce


def add(m, n):
    s = m + n
    return s


# [(1+2)+3]+4 = 10
result = reduce(add, [1, 2, 3, 4])
print(result)
# 2*[2*(2*5+1)+2]+3 = 51
result = reduce(lambda x, y: 2 * x + y, [1, 2, 3], 5)
print(result)
# iterable is empty return initial
result = reduce(lambda x, y: 10 * x + 2 * y, [], 123)
print(result)  # 123
# Return the first element in iterable
result = reduce(lambda x, y: 10 * x + 2 * y, [123])
print(result)  # 123
# 10*2 + 2*123 = 266
result = reduce(lambda x, y: 10 * x + 2 * y, [123], 2)
print(result)
