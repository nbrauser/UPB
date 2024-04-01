import os
from datetime import datetime
import calendar as cal

# get current working directory
# print(os.getcwd())


# change the directory
# os.chdir('C:\\Users\\nmb132\\OneDrive - University of Pittsburgh\\UPB')
# print(os.getcwd())

# list all the files at the current location
# print(os.listdir())

# create a new directory
# mkdir --> make a single directory
# makedirs --> make hierarchy of directories
# os.mkdir('Dir1')
# print(os.listdir())
#
# os.makedirs('dir2\\Dir2_1')
# print(os.listdir())

# remove the directories
# os.rmdir('dir2')
# os.removedirs('dir2\\Dir2_1')
# print(os.stat('test'))
# added_time = os.stat('test').st_atime
# print(datetime.fromtimestamp(added_time))

# print(cal.month(2024,4))
# print(cal.calendar(2026))

# print(cal.HTMLCalendar().formatmonth(2024,4))
