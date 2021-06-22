# -------------------------------------
# --- Date and time => introduction ---
# -------------------------------------

import datetime

# print(dir(datetime))
# print(dir(datetime.datetime))

# Print current date and time 
print(datetime.datetime.now())

print("=" * 10)

# Print current year 
print(datetime.datetime.now().year)

# Print current month 
print(datetime.datetime.now().month)

# Print current day 
print(datetime.datetime.now().day)


print("=" * 10)


# print(dir(datetime.datetime.now()))

# Print the current time 
print(datetime.datetime.now().time())

print("=" * 10)

# Print the current time hour
print(datetime.datetime.now().time().hour)

# Print the current time minute
print(datetime.datetime.now().time().minute)

# Print the current time second
print(datetime.datetime.now().time().second)


print("=" * 10)


# Print start and end of time 
print(datetime.time.min)
print(datetime.time.max)


print("=" * 10)


print(datetime.datetime(1446, 6, 3))
print(datetime.datetime(1446, 6, 3, 10, 45, 55, 153525))


print("=" * 10)


born_day = datetime.datetime(1446, 6, 3)
date_now = datetime.datetime.now()

print(f"My born day is {born_day} and ", end="")
print(f"date now is {date_now}")

print(f" I lived for {date_now - born_day}")
print(f" I lived for {(date_now - born_day).days} days")
