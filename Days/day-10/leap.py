def is_leap(year):
  """this function verifies if the year is a leap year or not."""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False
  
def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 2 and is_leap(year):
    return 29
  else:
    return month_days[month -1]
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

#if the year is leap and the month is febreaury, return 29 instead of 28. if not, return the month as month_days shows.

