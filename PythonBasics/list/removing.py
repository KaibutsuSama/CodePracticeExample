langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript", "Ruby"]
print(langs)

# lang = langs.pop(3)
# print("{0} was removed".format(lang))
#
# lang = langs.pop()
# print("{0} was removed".format(lang))
# print(langs)

langs.remove("Ruby")  # 只能移除一个
print(langs)
