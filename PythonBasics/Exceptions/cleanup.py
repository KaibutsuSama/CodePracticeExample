f = None

try:

    f = open('data.txt', 'r')
    contents = f.readlines()

    for line in contents:
        print(line.rstrip())

except IOError:

    print('Error opening file')

finally:

    if f:
        f.close()