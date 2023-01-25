def input_numbers():

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b

x, y = input_numbers()
print(f"{x} / {y} is {x/y}")