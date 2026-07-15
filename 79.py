from datetime import datetime
# datetime module 

# get current date and time 

now = datetime.now()
print(now)

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print("current date: ", now.date)
print("current time: ", now.strftime("%H:%M:%S"))
print("------------------")

# get month name
print(now.strftime("%B"))
print(now.strftime("%b"))

# get day name
print(now.strftime("%A"))
print(now.strftime("%a"))

print("program ended here")