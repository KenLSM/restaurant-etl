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

    days = map(decomposeByDays, days)
    # print(days)
    days = flatten(days)
    dayTime = map(lambda x: [x, time], days)
    dayTime = map(decomposeByTime, dayTime)
    print(dayTime)
    dayTime = flatten(dayTime)
    print(dayTime)
    return dayTime


def decomposeByTime(daytime):
    """
    Takes "0(Mon) 11pm - 12:30am

    Returns [[0, 11*60, 11*60+59], [1, 0, 30]]
    """

    def convertTimeToMinutes(time):
        [hrMin, period] = time.split(" ")
        extraMins = (12 * 60 if period == 'pm' else 0)
        # print(time)
        [hr, minute] = hrMin.split(":") if hrMin.find(":") > 0 else [hrMin, 0]

        # 12:30am should be regarded as 0039
        hr = 0 if period == 'am' and hr == '12' else hr
        # print(period)
        return int(hr) * 60 + int(minute) + extraMins

    [day, time] = daytime
    # print(daytime)
    [startTime, endTime] = map(lambda x: x.strip(), time.split("-"))

    startMinutes = convertTimeToMinutes(startTime)
    endMinutes = convertTimeToMinutes(endTime)
    if(endMinutes < startMinutes):
        print(startTime, endTime, startMinutes, endMinutes)
        print([
            [day, startMinutes, 23*60 + 59],
            [(day+1) % 7, 0, endMinutes],
        ])
        return [
            [day, startMinutes, 23*60 + 59],
            [(day+1) % 7, 0, endMinutes],
        ]
    return [[day, startMinutes, endMinutes]]


def decomposeByDays(days):
    """
    Takes "Mon-Thus" | "Sun"

    Returns [1, 2, 3, 4] | [7]
    """

    if days.find("-") < 0:
        return [DAYS_OF_WEEK.index(days)]

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
            # print(timing)
            a = transformTime2TimeMap(timing)
            a = flatten(a)
            a = map(lambda x: [name]+x, a)
            restWriter.writerows(a)
            # print(a)
