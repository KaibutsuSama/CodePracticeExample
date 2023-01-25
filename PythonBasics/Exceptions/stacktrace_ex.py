import traceback


def myfun():
    def myfun2():

        try:
            3 / 0
        except ZeroDivisionError as e:

            print(e)
            print("Class: ", e.__class__)

            for line in traceback.format_stack():
                print(line.strip())

    myfun2()


def test():
    myfun()


test()
