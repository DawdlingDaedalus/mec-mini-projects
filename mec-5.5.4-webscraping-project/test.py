import sqlite3
import json


# read json file
with open('/Users/p/Documents/GitHub/mec-mini-projects/mec-5.5.4-webscraping-project/mini_proj/xpath-scraper-results.json') as json_file:
    data = json.load(json_file)

for item in data:
    print(item)
