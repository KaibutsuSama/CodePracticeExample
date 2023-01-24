lang = "Python"

a = []

for e in lang:
    a.append(ord(e))

b = [ord(e) for e in lang]
print(a)
print(b)