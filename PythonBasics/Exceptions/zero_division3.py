def input_numbers():
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    return a, b


x, y = input_numbers()

try:
    print(x, "/", y, "=", x / y)

except ZeroDivisionError:
    print("Y Cannot be zero")
    x, y = input_numbers()

