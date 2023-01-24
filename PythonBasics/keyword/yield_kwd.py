def gen():
    x = 11
    yield x


it = gen()

print(it.__next__())
