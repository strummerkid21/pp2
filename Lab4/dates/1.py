from datetime import datetime, timedelta

# Subtract five days from the current date
def subtract_five_days():
    current_date = datetime.now()
    new_date = current_date - timedelta(days=5)
    return new_date.strftime('%Y-%m-%d')