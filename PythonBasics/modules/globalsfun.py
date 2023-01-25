import textwrap

version = 1.0


def myfun():
    pass


gl = globals()
gnames = ', '.join(gl)

print(textwrap.fill(gnames))
print()
print(gnames)