import csv
import re
import pprint
from itertools import chain
import pdb


timeRegex = r'(?<=[a-z])\s(?=[0-9])'
DAYS_OF_WEEK = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


def flatten(arr):
    return list(chain(*arr))


def resolveDayRange(s):
    days, time = re.split(timeRegex, s)
    time = time.strip()
    days = days.split(",")
    days = map(lambda x: x.strip(), days)

    days = map(decomposeDays, days)
    # print(days)
    days = flatten(days)
    dayTime = map(lambda x: [x, time], days)
    return dayTime


def decomposeDays(days):
    """
    Takes "Mon-Thus" | "Sun"

    Returns [1, 2, 3, 4] | [7]
    """

    if days.find("-") < 0:
        return days

    start, end = days.split("-")
    start = DAYS_OF_WEEK.index(start)
    end = DAYS_OF_WEEK.index(end)
    if end < start:
        end += 7
    decomposed = map(lambda x: x % 7, range(start, end + 1))
    return decomposed


def transformTime2TimeMap(timing):
    timeList = timing.split("/")

    timeList = map(resolveDayRange, timeList)

    return timeList


with open('input.csv', 'r') as csvRead:
    restReader = csv.reader(csvRead)
    with open('output.csv', 'a') as csvWrite:
        restWriter = csv.writer(csvWrite)

        for [name, timing] in restReader:
            a = transformTime2TimeMap(timing)
            a = flatten(a)
            a = map(lambda x: [name]+x, a)
            restWriter.writerows(a)
            print(a)
