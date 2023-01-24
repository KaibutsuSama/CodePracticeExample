a1 = ["bear", "lion", "tiger", "eagle"]
a2 = ["bear", "lion", "tiger", "eagle"]
a3 = ["bear", "lion", "tiger", "eagle"]

a1.reverse()
print(a1)

it = reversed(a2)
r = list()

for e in it:
    r.append(e)

print(r)

print(a3[:1])