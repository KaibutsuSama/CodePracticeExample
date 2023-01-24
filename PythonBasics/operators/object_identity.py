print(None == None)
print(None is None)

print(True is True)

print([] == [])
print([] is [])
#输出可能会让您感到惊讶。 在 Python 语言中，只有一个None和一个True对象。 这就是True相等且与True相同的原因。
# 无论如何，那里只有一个真理。 空列表[]等于另一个空列表[]。 但是它们并不相同。 Python 已将它们放入两个不同的内存位置。
# 它们是两个不同的对象。 因此，is运算符返回False。
print("Python" == "Python")
