def power(x, y=2):
    r = 1
    for i in range(y):
        r *= x

    return r


print(power(3))
print(power(3, 5))
print(power(5, 5))
