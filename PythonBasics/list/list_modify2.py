first = [1, 2, 3]
second = [4, 5, 6]

first.extend(second)
print(first)  # [1, 2, 3, 4, 5, 6]

first[0] = 11
first[1] = 22
first[2] = 33
print(first)  # [11, 22, 33, 4, 5, 6]

print(first.pop(5))
print(first)