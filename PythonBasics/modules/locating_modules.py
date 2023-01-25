import sys
import textwrap

sp = sorted(sys.path)
dnames = ', '.join(sp)

print(textwrap.fill(dnames))