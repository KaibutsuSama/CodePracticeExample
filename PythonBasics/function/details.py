def display(**details):
    for i in details:
        print(f"{i}: {details[i]}")


display(name="Larry", age=43, sex="M")
