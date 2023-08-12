"""
You receive a date and need to know what day of the week it is. 
 
Task: 
Create a program that takes in a string containing a date, and outputs the day of the week.

Input Format: 
A string containing a date in either "MM/DD/YYYY" format or "Month Day, Year" format.

Output Format: 
A string containing the day of the week from the provided date.

Sample Input: 
11/19/2019

Sample Output: 
Tuesday

Explanation: 
19 November 2019 is a Tuesday.
"""
from datetime import datetime 
import calendar
date = input()
if '/' in date:
    dateform = datetime.strptime(date, '%m/%d/%Y')
else:
    dateform = datetime.strptime(date, '%B %d, %Y')
weekdy = datetime.weekday(dateform)
print(calendar.day_name[weekdy])
