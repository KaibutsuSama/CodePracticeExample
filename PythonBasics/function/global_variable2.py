name = "Jack"


def f():
    global name
    name = "Robert"
    print("Within function", name)


print("Outside function", name)
f()
print("Outside function", name)
