import os

try:
    os.mkdir('newdir')
    print('directory created')
except (FileExistsError, RuntimeError) as e:
    print(e)
