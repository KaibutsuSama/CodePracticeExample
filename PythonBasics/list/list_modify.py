names = []

names.append("Ashe")
names.append("SmallYi")
names.append("Gk")
names.append("OldXu")
print(names)  # ['Ashe', 'SmallYi', 'Gk', 'OldXu']

names.insert(0, "TigerBro")
print(names)

names.remove("OldXu")
print(names)
names.remove("Ashe")
print(names)

del names[1]
print(names)

del names[0]
print(names)

del names[0]
print(names)