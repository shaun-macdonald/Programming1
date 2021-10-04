#Challange3 Week 1

user = int(input("Enter total seconds for duration: "))

days = 86400
hours = 3600
minutes = 60
seconds = 1

days1 = user // days
days2 = user % days

if days1 < 10:
    days1 = "0" + str(days1)

hours1 = days2 // hours
hours2 = days2 % hours
if hours1 < 10:
    hours1 = "0" + str(hours1)


minutes1 = hours2 // minutes
minutes2 = hours2 % minutes
if minutes1 < 10:
    minutes1 = "0" + str(minutes1)



seconds1 = minutes2 // seconds
seconds2 = minutes2 % seconds
if seconds1 < 10:
    seconds1 = "0" + str(seconds1)


print("Total is {} days, {} hours, {} minutes, {} seconds".format(days1, hours1, minutes1, seconds1))