with open('works.txt', 'r') as f:
    print(f.read(14))
    print(f"The current file position is {f.tell()}")

    f.seek(0, 0)

    print(f.read(30))
