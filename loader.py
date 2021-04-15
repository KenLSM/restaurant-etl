import csv
import requests
from functools import lru_cache

DB_URL = 'http://localhost:8082/core'

GET_RESTAURANTS_BY_NAME = 'CMD_GET_RESTAURANTS_BY_NAME'
UPSERT_RESTAURANTS = 'CMD_UPSERT_RESTAURANT'


a = requests.get(DB_URL + '/' + GET_RESTAURANTS_BY_NAME + '?name=ke').json()


@lru_cache(maxsize=None)
def upsertRestaurants(name):
    resp = requests.get(DB_URL + '/' + UPSERT_RESTAURANTS +
                        '?name=' + name).json()
    print(resp)


with open('output.csv') as csvFile:
    entries = csv.reader(csvFile)
    for row in entries:
        [name, day, startMinutes, endMinutes] = row
        upsertRestaurants(name)
