items = {"coins": 7, "pens": 3, "cups": 2,
         "bags": 1, "bottles": 4, "books": 5}

for key, value in sorted(items.items(), key=lambda pair: pair[1]):
    print("{0}: {1}".format(key, value))

print("###############")

for key, value in sorted(items.items(), key=lambda pair: pair[1], reverse=True):
    print("{0}: {1}".format(key, value))
