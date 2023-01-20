import sys

print("script name: ", sys.argv[0])
print("Argument: ", end=" ")
for arg in sys.argv[1:]:
    print(arg, end=" ")

print()