try:
    a = (1, 2, 3, 4)
    print(a[5])
except IndexError as e:

    print(e)
    print("Class:", e.__class__)
