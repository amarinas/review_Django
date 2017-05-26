import random

# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h"
str = "string"


def random_item(iterable):
  return iterable[random.randint(0,len(iterable)-1)]


print(random_item("Treehouse"))
