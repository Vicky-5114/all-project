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
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b
