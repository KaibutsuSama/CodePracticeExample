langs = []
langs.append("Python")
langs.append("Per1")
print(langs)

langs.insert(0, "PHP")
langs.insert(2, "Lua")
print(langs)

langs.extend(("JavaScript", "ActionScript"))  # extend()方法将值的序列添加到列表的末尾。 在我们的例子中，两个 Python 元组字符串附加在列表的末尾。
print(langs)

# ['Python', 'Per1']
# ['PHP', 'Python', 'Lua', 'Per1']
# ['PHP', 'Python', 'Lua', 'Per1', 'JavaScript', 'ActionScript']