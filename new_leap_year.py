def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return("Leap year")
      else:
        return("Not leap year")
    else:
      return("Leap year")
  else:
    return("Not leap year")
  
# TODO: Add more code here 👇
def days_in_month(year, month):
  is_year_leap = is_leap(year)

  if is_year_leap == "Not leap year":
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    month_in_days = month_days[month-1]
    return month_in_days
  else:
     month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
     month_in_days = month_days[month-1]
     return month_in_days

  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

