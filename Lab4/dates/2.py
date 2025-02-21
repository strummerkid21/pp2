from datetime import datetime, timedelta
def print_days():
    today = datetime.now()
    yesterday = today - timedelta(days=1)
    tomorrow = today + timedelta(days=1)
    print(f"Yesterday: {yesterday.strftime('%Y-%m-%d')}")
    print(f"Today: {today.strftime('%Y-%m-%d')}")
    print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")