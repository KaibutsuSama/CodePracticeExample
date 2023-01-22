n = [1, 2, 3, 4, 5]

try:
    n[0] = 10
    n[6] = 60  # Error
    print(n[5])  # Error

except IndexError as e:
    print(e)
