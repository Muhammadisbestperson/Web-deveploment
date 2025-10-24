import random
from datetime import datetime, timedelta

def getRandomDate(start, end):
    dateformat = "%m/%d/%Y"
    start_date = datetime.strptime(start, dateformat)
    end_date = datetime.strptime(end, dateformat)
    
    # Calculate a random number of days between start and end
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    
    random_date = start_date + timedelta(days=random_days)
    return random_date.strftime(dateformat)

print("Random Date =", getRandomDate("1/1/2024", "10/28/2025"))
