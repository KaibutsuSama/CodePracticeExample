def to_upper(s):
    return s.upper()


words = ["stone", "cloud", "dream", "sky"]

words2 = list(map(to_upper, words))

print(words2)

