import sys

print('Enter your name: ', end='')

name = ''

sys.stdout.flush()

while True:

    c = sys.stdin.read(1)

    if c == '\n':
        break

    name += c

print('Your name is: ', name)
