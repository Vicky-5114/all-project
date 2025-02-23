list_original = [1, 2, 3]
list_1 = list_original.copy()

for item in list_1:
    # idx:  0, 1, 2
    # elem: 1, 2, 3
    # 1) Remove idx:0 -> 1
    # 2) Remove idx:1 -> 3
    list_1.remove(item)

# Remain: 2
print(list_1)


list_2 = list_original[:]
print(list_2)  # [1, 2, 3]
list_2 = list_2[:1] + list_2[2:]
print(list_2)  # [1, 3]
