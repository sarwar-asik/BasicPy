import datetime

x= datetime.datetime(2020,5,17)
print(x)

currentTime = datetime.datetime.now()
print(currentTime)
print('weakday short', currentTime.strftime("%a"))
print('weakday full', currentTime.strftime("%A"))
print('day of month', currentTime.strftime("%d"))
print('month number', currentTime.strftime("%m"))
print('am/pm time', currentTime.strftime("%p"))




