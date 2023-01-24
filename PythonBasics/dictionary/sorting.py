items = {"coins": 7, "pens": 3, "cups": 2,
         "bags": 1, "bottles": 4, "books": 5}

for key in sorted(items.keys()):
    print("{0}: {1}".format(key, items[key]))

print("###############")

for key in sorted(items.keys(), reverse=True):
    print("{0}: {1}".format(key, items[key]))
