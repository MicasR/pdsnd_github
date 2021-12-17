from datetime import datetime


def str_is_date(date_string: str, format: str = "%Y-%m-%d") -> bool:
    """Check if str is in the correct date format"""
    if type(date_string) != str: return False
    try:
        datetime.strptime(date_string, format)
        return True
    except ValueError:
        return False


def is_positive_float(item: str) -> bool:
    """Check if item is a positive float."""
    try:
        if float(item) <  0: return False
        if float(item) >= 0: return True
    except:
        return False


def float_to_str_date(seconds: float) -> str:
    """transform seconds to date string"""
    seconds_in_day = 60 * 60 * 24
    seconds_in_hour = 60 * 60
    seconds_in_minute = 60

    days = seconds // seconds_in_day
    hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
    minutes = (seconds - (days * seconds_in_day) -
            (hours * seconds_in_hour)) // seconds_in_minute
    seconds_ = seconds % 60

    time_str = ""

    if days != 0: time_str = time_str + str(int(days)) + "d "
    if hours != 0: time_str = time_str + str(int(hours)) + "h "
    if minutes != 0: time_str = time_str + str(int(minutes)) + "m "
    if seconds_ != 0 : time_str = time_str + str(int(seconds_)) + "s "

    return time_str.strip()


