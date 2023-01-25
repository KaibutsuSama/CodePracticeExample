import random
import itertools

for i in itertools.count():

   val = random.randint(1, 30)
   print(val)

   if (val == 22):
      break