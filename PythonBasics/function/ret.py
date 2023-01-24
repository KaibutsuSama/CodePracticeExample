def show_module_nmae():
    print(__doc__)


def get_module_name():
    return __file__


a = show_module_nmae()
b = get_module_name()

print(a)
