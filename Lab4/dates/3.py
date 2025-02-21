from datetime import datetime, timedelta
def drop_microseconds():
    now = datetime.now().replace(microsecond=0)
    return now
