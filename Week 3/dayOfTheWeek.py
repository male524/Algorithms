# 1185. Day of the Week
"""
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the day, month and year respectively.

Return the answer as one of the following values {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.

 

Example 1:

Input: day = 31, month = 8, year = 2019
Output: "Saturday"
Example 2:

Input: day = 18, month = 7, year = 1999
Output: "Sunday"
Example 3:

Input: day = 15, month = 8, year = 1993
Output: "Sunday"
 

Constraints:

The given dates are valid dates between the years 1971 and 2100.
"""

import datetime


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        daysOfWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekDay = datetime.datetime(year, month, day).weekday()
        return daysOfWeek[weekDay]

# I learned how to use the datetime library to get the weekday of a given date.
# This took me around 30 minutes since I found this library and had to look through the documentation to figure out how it worked.