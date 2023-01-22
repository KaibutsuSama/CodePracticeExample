n = [1, 2, 3, 4, 5]

try:
    print(n['1'])
except TypeError as e:
    print("Error in file {0}".format(__file__))
    print("Message: {0}".format(e))