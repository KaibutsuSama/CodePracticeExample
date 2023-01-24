from time import strftime, gmtime


def show_message(msg):
    print(msg)


show_message("Ready.")


def show_message(msg):
    print(strftime("%H:%M:%S"), gmtime())
    print(msg)


show_message("Progressing")
