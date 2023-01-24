class YesNoException(Exception):

    def __init__(self):
        print("This is not a yes or no answer")


answer = 'y'

if (answer != 'Yes' and answer != 'no'):
   raise YesNoException

else:
    print()