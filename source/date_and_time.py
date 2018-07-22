# Retrieves the current date and time

from datetime import datetime
dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S').split(' ')
current_date = dt[0]
current_time = dt[1]
print(current_date)
print(current_time)
