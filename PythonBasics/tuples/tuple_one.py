print((3 + 7))  # 不是元组
print((3 + 7,))  # 是元组

notTuples = (3 + 7)
isTuples = ((3 + 7, 4 + 7, 5 + 7))

print(type(notTuples))  # int
print(type(isTuples))  # tuple
