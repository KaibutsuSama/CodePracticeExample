def input_numbers():

    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b

x, y = input_numbers()

while True:

    if y != 0:

        print(f"{x} / {y} is {x/y}")
        break

    else:

        print("Cannot divide by zero")
        x, y = input_numbers()