num = 0

for num in range(1000):

    num += 1

    if (num % 2) == 0:
        continue

    print(num, end=" ")

print()
