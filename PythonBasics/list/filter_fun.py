def positive(x):
    return x > 0

n = [-2, 0, 1, 2, -3, 4, 4, -1]

print(list(filter(positive, n)))