from datetime import datetime, timedelta

class MeetupDayException(Exception):
    pass

def meetup_day(year, month, day, which):
    if not is_valid(which):
        raise MeetupDayException

    if is_edge_case(which):
        return date_for_edge_case(year, month, day, which)

    try:
        return regular_date(year, month, day, which)
    except MeetupDayException as exception:
        raise exception

def is_valid(which):
    return which in ['teenth', 'last', '1st', '2nd', '3rd', '4th', '5th']

def is_edge_case(which):
    return which in ['teenth', 'last']

def date_for_edge_case(year, month, day, which):
    assert(is_edge_case(which))

    if which == 'teenth':
        return teenth(year, month, day)

    if which == 'last':
        return last(year, month, day)

def regular_date(year, month, day, which):
    date = datetime(year, month, 1)

    while date.weekday() != weekday_conversion(day):
        date += timedelta(1)
    
    index = ['1st', '2nd', '3rd', '4th', '5th'].index(which)
    for i in range(index):
        date += timedelta(7)
    
    if date.month != month: raise MeetupDayException
    return date.date()

def teenth(year, month, day):
    return edge_case(year, month, 13, day)

def last(year, month, day):
    return edge_case(year, month, last_day(year, month) - 6, day)

def edge_case(year, month, start_date, day):
    date = datetime(year, month, start_date)
    date += timedelta((weekday_conversion(day) - date.weekday()) % 7)
    return date.date()

def last_day(year, month):
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_lengths[month - 1] + is_leap_month(year, month)

def is_leap_month(year, month):
    return month == 2 and is_leap_year(year)

def is_leap_year(year):
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)

def weekday_conversion(weekday):
    day_conversions = {
        'Monday': 0, 
        'Tuesday': 1, 
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday':5,
        'Sunday': 6
    }
    return day_conversions.get(weekday, -1)