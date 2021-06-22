# --------------------------------------------------------
# ----------- Practical age full details -----------------
# --------------------------------------------------------

# Write note 
print("-" * 80)
print(" You can write the first letter or full name of the time unit ".center(80, '-'))
print("-" * 80)

# Collect age data 
age = input("Please write your age ").strip()

# Collect time unit 
unit = input("Please choose time unit : monthes, weeks, days ").strip().lower()  # Remove spaces and make all characters small 

# Get time units 

months = int(age) * 12
weeks = months * 4
days = int(age) * 364 

if unit == "months" or unit == "m": 

    print("You choosed the unit months")
    print(f"You lived for {months:,} months.")

elif unit == "weeks" or unit == "w": 

    print("You choosed the unit weeks")
    print(f"You lived for {weeks:,} weeks.")

elif unit == "days" or unit == "d": 

    print("You choosed the unit days")
    print(f"You lived for {days:,} days.")

