langs = ["Python", "Ruby", "Perl", "Lua", "JavaScript"]
print(langs)

del langs[1]
print(langs)

# del langs[15] # 我们只能删除现有元素。 如果取消注释代码行，我们将收到IndexError消息。

del langs[:]
print(langs)
