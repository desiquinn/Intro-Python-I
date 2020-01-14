"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

curr_month = datetime.today().month
curr_year = datetime.today().year

def print_cal(month = curr_month, year = curr_year):
    if 0 < month < 13:
        print(calendar.month(year, month, 2, 1))
    else:
      print('The month must be a number between 1 and 12')

# cal_input = input("~~> ").split(",")

# if len(cal_input) == 0:
#     print_cal()
# elif len(cal_input) == 1:
#     print_cal(int(cal_input[0]))
# elif len(cal_input) == 2:
#     print_cal(int(cal_input[0]), int(cal_input[1]))
# else:
#     print("input must include a month(1-12), or a month and year (2, 1986)")

# to make this better I would validate the year as well and return an error

# How i would solve it with .argv instead of the input()
if len(sys.argv) == 1:
    print_cal()
elif len(sys.argv) == 2:
    print_cal(int(sys.argv[1]))
elif len(sys.argv) == 3:
    print_cal(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("input must include a month(1-12), or a month and year (2, 1986)")
    