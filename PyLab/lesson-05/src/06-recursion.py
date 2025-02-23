# Seq:   0, 1, 1, 2, 3, ...
# Index: 0, 1, 2, 3, 4, ...

# F(n) = F(n-1) + F(n-2)


def febbonaci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return febbonaci_recursive(n - 1) + febbonaci_recursive(n - 2)


def febbonaci_iterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def hanoi(n, src, helper, target):
    if n == 1:
        print(f"Move Disk 1 from {src} to {target}")
        return 1
    x = hanoi(n - 1, src, target, helper)
    print(f"Move Disk {n} from {src} to {target}")
    y = hanoi(n - 1, helper, src, target)
    return x + y + 1


# Loop from 1 to 4
for i in range(1, 5):
    print(f"====== Total Steps: {hanoi(i, "stick-1", "stick-2", "stick-3")} ======")


def func(m):
    m0 = 1
    m1 = 1
    for _ in range(m - 1):
        m0, m1 = m1, m0 + m1
    return m1


for i in range(10):
    print(func(i))


def get_rabbits(m):
    if m < 2:
        return 1
    return get_rabbits(m - 1) + get_rabbits(m - 2)


print(get_rabbits(999))

import sys

print(sys.getrecursionlimit())
sys.setrecursionlimit(1500)
print(get_rabbits(999))

store = {}


def get_rabbits(m):
    if m < 2:
        return 1
    if m in store:
        return store[m]
    result = get_rabbits(m - 1) + get_rabbits(m - 2)
    store[m] = result
    return result
