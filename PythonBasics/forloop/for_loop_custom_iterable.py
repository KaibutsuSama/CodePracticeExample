import random


def myrandom(x):
    i = 0

    while i < x:
        r = random.randint(0, 100)

        yield r
        
        i += 1


for r in myrandom(5):
    print(r)
