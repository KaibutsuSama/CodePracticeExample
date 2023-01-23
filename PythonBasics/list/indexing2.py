# index(e, start, end)方法查找特定元素并返回其最低索引。 start和end是可选参数，它们将搜索限制到给定的边界。
n = [1, 2, 3, 4, 1, 2, 3, 1, 2]

print(n.index(1))  # 0
print(n.index(2))  # 1

print(n.index(1, 1))  # 4
print(n.index(2, 2))  # 5

print(n.index(1, 2, 5))  # 4
print(n.index(3, 4, 8))  # 6
