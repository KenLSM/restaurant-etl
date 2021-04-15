import csv
import requests
from functools import lru_cache
from urllib.parse import urlencode

DB_URL = 'http://localhost:8082/core'

GET_RESTAURANTS_BY_NAME = 'CMD_GET_RESTAURANTS_BY_NAME'
UPSERT_RESTAURANTS = 'CMD_UPSERT_RESTAURANT'

SET_OPENING_TIME = 'CMD_SET_OPENING_TIME'

a = requests.get(DB_URL + '/' + GET_RESTAURANTS_BY_NAME + '?name=ke').json()


@lru_cache(maxsize=None)
def upsertRestaurants(name):
    print(name, urlencode({'name': name}))
    resp = requests.get(DB_URL + '/' + UPSERT_RESTAURANTS + '?' +
                        urlencode({'name': name})).json()
    print(resp)


def setOpeningTime(entry):
    print(entry, urlencode(entry))
    resp = requests.get(DB_URL + '/' + SET_OPENING_TIME + '?' +
                        urlencode(entry)).json()
    print(resp)


with open('output.csv') as csvFile:
    entries = csv.reader(csvFile)
    for row in entries:
        datum = {
            'name': row[0],
            'day': row[1],
            'startMinutes': row[2],
            'endMinutes': row[3],
        }
        upsertRestaurants(datum['name'])
        setOpeningTime(datum)
