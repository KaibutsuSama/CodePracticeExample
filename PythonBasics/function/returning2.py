n = [1, 2, 3, 4, 5]


def stats(x):
    _mx = max(x)
    _mn = min(x)
    _ln = len(x)
    _sm = sum(x)

    return _mx, _mn, _ln, _sm


mx, mn, ln, sm = stats(n)
print(stats(n))

print(mx, mn, ln, sm)

