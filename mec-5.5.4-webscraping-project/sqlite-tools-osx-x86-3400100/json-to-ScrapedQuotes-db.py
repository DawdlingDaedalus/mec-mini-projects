import sqlite3
import json


def switch(myint):
    if myint == 0:
        return cursor.execute('''insert into quotes (id, quote, author) 
                              values (?, ?, ?)''',
                              (counter_id, item['text'], item['author']))
    elif myint == 1:
        return cursor.execute('''insert into quotes (id, quote, author, tag1) 
                              values (?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0]))
    elif myint == 2:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2) 
                              values (?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1]))
    elif myint == 3:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2, tag3) 
                              values (?, ?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1], item['tags'][2]))
    elif myint == 4:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2, tag3, tag4) 
                              values (?, ?, ?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1], item['tags'][2], item['tags'][3]))
    elif myint == 5:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2, tag3, tag4, tag5) 
                              values (?, ?, ?, ?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1], item['tags'][2], item['tags'][3], item['tags'][4]))
    elif myint == 6:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2, tag3, tag4, tag5, tag6) 
                              values (?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1], item['tags'][2], item['tags'][3], item['tags'][4], item['tags'][5]))
    elif myint == 7:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2, tag3, tag4, tag5, tag6, tag7) 
                              values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1], item['tags'][2], item['tags'][3], item['tags'][4], item['tags'][5], item['tags'][6]))
    elif myint == 8:
        return cursor.execute('''insert into quotes (id, quote, author, tag1, tag2, tag3, tag4, tag5, tag6, tag7, tag8) 
                              values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                              (counter_id, item['text'], item['author'], item['tags'][0], item['tags'][1], item['tags'][2], item['tags'][3], item['tags'][4], item['tags'][5], item['tags'][6], item['tags'][7]))


# connect to db & create cursor
conn = sqlite3.connect(
    '/Users/p/Documents/GitHub/mec-mini-projects/mec-5.5.4-webscraping-project/sqlite-tools-osx-x86-3400100/ScrapedQuotes.db')
cursor = conn.cursor()

# read json file
with open('/Users/p/Documents/GitHub/mec-mini-projects/mec-5.5.4-webscraping-project/mini_proj/xpath-scraper-results.json') as json_file:
    data = json.load(json_file)

counter_id = 0
for item in data:
    counter_id += 1
    tags_len = len(item['tags'])
    switch(tags_len)


conn.commit()
conn.close()
