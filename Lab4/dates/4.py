from datetime import datetime, timedelta
def date_difference_in_seconds(date1, date2):
    delta = date2 - date1
    return delta.total_seconds()