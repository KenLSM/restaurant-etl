import csv
import re

timeRegex = r'(?<=[a-z])\s(?=[0-9])'
DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def resolveDayRange(s):
    days, time = re.split(timeRegex, s)
    time = time.strip()
    days = days.split(",")
    days = map(lambda x: x.strip(), days)

    days = map(decomposeDays, days)
    print(list(days), time)

    return []


def decomposeDays(days):
    if not days.find("-"):
        return days

    days = days.split("-")
    days = map(lambda x: DAYS_OF_WEEK.find(x), days)
    return days


def transformTime2TimeMap(timing):
    timeList = timing.split("/")

    vv = map(resolveDayRange, timeList)
    print(list(vv))
    # hasMultiDay = filter(checkMultiDay, timeList)
    # print(list(hasMultiDay))
    return timeList


"Mon-Thu, Sun 11:30 am - 9:30 pm"


"Mon 11:30 am - 9:30 pm"
"Tue 11:30 am - 9:30 pm"
"Wed 11:30 am - 9:30 pm"
"Thu 11:30 am - 9:30 pm"
"Sun 11:30 am - 9:30 pm"

transformTime2TimeMap("Mon-Thu, Sun 11:30 am - 9:30 pm")
# with open('input.csv', 'r') as csvfile:
#     restReader = csv.reader(csvfile)
#     for [name, timing] in restReader:
#         transformTime2TimeMap(timing)
#         # print(name, )
