import copy

w = ["Python", "Ruby", "Perl"]

c1 = w[:]
c2 = list(w)
c3 = copy.copy(w)
c4 = copy.deepcopy(w)
c5 = [e for e in w]

c6 = []

for e in w:
    print(e)
    c6.append(e)

c7 = []
c7.extend(w)

print(c1)
print(c2)
print(c3)
print(c4)
print(c5)
print(c6)
print(c7)