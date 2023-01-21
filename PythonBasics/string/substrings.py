#!/usr/bin/env python

# substrings.py

a = "I saw a wolf in the forest. A lone wolf."

print(a.find("wolf"))  # 8
print(a.find("wolf", 10, 20))  # -1
print(a.find("wolf", 15))  # 35

print(a.rfind("wolf"))  # 35
