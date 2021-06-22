# ----------------------------------
# -- Date and time => format date --
# ----------------------------------
# https://strftime.org/
# ----------------------------------

import datetime

my_born_date = datetime.datetime(1446, 6, 3)

print(my_born_date)
print(my_born_date.strftime("%a"))
print(my_born_date.strftime("%A"))
print(my_born_date.strftime("%b"))
print(my_born_date.strftime("%B"))

print("=" * 10)

print(my_born_date.strftime("%d %B %Y"))
print(my_born_date.strftime("%d, %B, %Y"))
print(my_born_date.strftime("%d/%B/%Y"))
print(my_born_date.strftime("%B %Y"))
