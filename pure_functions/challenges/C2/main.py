"""
Sort Dates
Datetimes are infamously a pain in the neck for programming. The least of the list of problems are the order of the year, month and day of a calendar date. Some countries use day-month-year format, others use year-month-day. Some insane countries use month-day-year because they want everyone else to be miserable.

Assignment
Fix the sort_dates function. It takes as input a list of dates in "MONTH-DAY-YEAR" format and returns a list of the dates sorted in ascending order.

Tip
The built-in sorted function might work better here than the .sort() list method. Create some function to transform the dates to more easily compare them with the sorted function.
"""

def sort_dates(dates):
    return sorted(dates, key = format_date)


def format_date(date):
    month, day, year = date.split("-")
    return year + month + day
