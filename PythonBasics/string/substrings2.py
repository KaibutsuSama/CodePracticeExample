a = "I saw a wolf in the forest. A lone wolf."

print(a.index("wolf"))
print(a.rindex("wolf"))

try:
    print(a.rindex("fox"))
except ValueError as e:
    print("Could not find substring")