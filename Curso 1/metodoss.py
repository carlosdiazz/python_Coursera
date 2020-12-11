
import datetime

ahora=datetime.datetime.now()

print(ahora.year)
print(ahora.month)
print(ahora.day)
print(ahora.hour)

print(ahora + datetime.timedelta(days=28))