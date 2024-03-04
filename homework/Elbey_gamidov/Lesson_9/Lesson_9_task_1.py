import datetime


my_time = "Jan 15, 2023 - 12:05:33"
reform_date = datetime.datetime.strptime(my_time, '%b %d, %Y - %H:%M:%S')
print(reform_date)
print(reform_date.strftime('%B'))
human_date = reform_date.strftime('%d.%m.%Y, %H:%M')
print(human_date)
