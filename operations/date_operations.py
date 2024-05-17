# import datetime
from datetime import date, datetime


def get_current_date():
    return date.today()


def calculate_date_difference(date1, date2):
    date1 = datetime.strptime(date1, "%Y-%m-%d")
    date2 = datetime.strptime(date2, "%Y-%m-%d")

    # Calculate the difference between the two dates
    date_difference = date2 - date1

    # Extract the number of days from the difference
    days_difference = date_difference.days
    return days_difference


def format_date(date, format):
    return date.strftime(format)
