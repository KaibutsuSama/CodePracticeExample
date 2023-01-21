first = [1, 2, 3]
second = (4, 5, 6)

print(tuple(first))  # (1, 2, 3)
print(list(second))  # [4, 5, 6]

print(first)  # [1, 2, 3]
print(second)  # (4, 5, 6)

# 我们可以使用tuple()函数从列表中创建一个元组，
# 并使用list()函数从元组中创建一个列表。
# 注意原始对象没有被修改； 函数仅返回那些转换后的集合。
