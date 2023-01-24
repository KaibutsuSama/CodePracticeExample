f = None

try:
    f = open('flims', 'r')

    for i in f:
        print(i,end="")

except IOError:

    print("Error reading File")

finally:

    if f:
        f.close()