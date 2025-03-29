from datetime import datetime, timedelta

def fivedays():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    return new_date.strftime('%Y-%m-%d')