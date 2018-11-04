from datetime import datetime, timedelta

def add_gigasecond(birth_date):
    return add(birth_date, 10 ** 9)

def add(birth_date, time_in_seconds):
    return birth_date + timedelta(seconds=time_in_seconds)
