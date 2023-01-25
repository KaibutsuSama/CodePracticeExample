class BFoundEx(Exception):

    def __init__(self, value):
        self.par = value

    def __str__(self):
        return f"BFoundEx: b character found at position {self.par}"


string = "There are beautiful trees in the forest."

pos = 0

for i in string:

    try:
        if i == 'b':
            raise BFoundEx(pos)
        pos = pos + 1

    except BFoundEx as e:
        print(e)
