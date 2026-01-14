from datetime import datetime

date1 = datetime(2026, 1, 1)
date2 = datetime(2026, 1, 14)

delta = date2 - date1
print(delta)
print(delta.days)
print(type(delta))
