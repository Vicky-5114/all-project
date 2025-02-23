a = 1, 2, 3, 4
print(a)  # (1, 2, 3, 4)

a = (1, 2, 3, 4)
print(a)  # (1, 2, 3, 4)

a, b, c, d = (1, 2, 3, 4)
print(a, b, c, d)  # 1 2 3 4

a, b, *c, d = (1, 2, 3, 4, 5)
print(a, b, c, d)  # 1 2 [3, 4] 5

a, b, *c, d = (1, 2, 3, 4)
print(a, b, c, d)  # 1 2 [3] 4

a, b, *c, d = (1, 2, 3)
print(a, b, c, d)  # 1 2 [] 3

(*a,) = (1, 2, 3, 4, 5)
print(a)  # [1 2 3 4 5]
print(*a)  # 1 2 3 4 5
