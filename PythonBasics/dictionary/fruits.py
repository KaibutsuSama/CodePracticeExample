basket = ('oranges', 'pears', 'apples', 'bananas')
print(basket)
fruits = {}.fromkeys(basket, 0)
print(fruits)

fruits['oranges'] = 12
fruits['pears'] = 8
fruits['apples'] = 4

print(fruits.setdefault('oranges', 11))
print(fruits.setdefault('kiwis', 11))

print(fruits)
