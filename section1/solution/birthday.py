"""
Write a program that first takes the year, month (as integer), and day of the user's birth date from console.
Then, calculate and print on which day of the year the user has been born.
You can assume user will enter a valid value for all inputs.
Example:
Enter your birth year: 1998
Enter your birth month as integer (Jan=1, Feb=2, ...): 9
Enter your birth day of the month: 21
You are born at the 264th day of the year 1998.
Hint: You may want to utilize your solution to leapyear problem.
"""

year = int(input('Enter your birth year: '))
month = int(input('Enter your birth month as integer (Jan=1, Feb=2, ...): '))
day = int(input('Enter your birth day of the month: '))

days = 0

# Part I: add days from the past months

complete_months = month - 1

# We will assume february has 30 days for now and correct later
# Number of days in each month: 31,30,31,30,31,30,31,31,30,31,30,31
# If we combine the pairs: 61,61,61,62,61,61

pairs = complete_months // 2

days += pairs * 61
# if number of pairs is bigger than 3, we need to add 1 since 4th pair has 62 days
if pairs > 3:
    days += 1

# we need to add the latest month if it's not included in pairs, i.e, complete_monts % 2 != 0
if complete_months % 2 != 0:
    # months 1, 3, 5, 7 has 31 days
    if complete_months < 8:
        days += 31
    # months 9, 11 has 30 days
    else:
        days += 30


# Part II: Correct for the February assumption (we assumed Feb has 30 days in Part I)

# If the year is a leap year we need to substract 1
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    days -= 1
# If its a common we need to substract 2
else:
    days -= 2

# Part III: Add the days of the current month
days += day

print('You are born at the ' + str(days) +
      'th day of the year ' + str(year) + '.')
