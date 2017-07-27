# python

import requests
import datetime
import sqlite3

email = '' # instapaper login
passwd = ''
safaridb = './WebpageIcons.db' #  from ~/Library/Safari/WebpageIcons.db

def test_auth(username, password):
    url = 'https://www.instapaper.com/api/authenticate'
    payload = {
        'username': username,
        'password': password
    }
    auth = requests.get(url, params=payload)
    print(auth.status_code) #200이 출력이 되지 않으면 아이디/비밀번호 에러
    return

def add_article(username, password, dbfile):
    # SQL load
    con = sqlite3.connect(dbfile)
    cursor = con.cursor()
    cursor.execute("SELECT url FROM PageURL")
    data = cursor.fetchall()
    # init
    url = 'https://www.instapaper.com/api/add'
    count = 0
    elapsed = datetime.datetime.fromtimestamp(0)

    for urls in range(len(data)):
        payload = {
          'username': username,
          'password': password,
          'url': data[urls][0]
          }
        r = requests.get(url, params=payload)
        count = count + 1
        print("%d - %d - %s" % (count, r.status_code, data[urls][0][:40]))
        # status code가 201이 나와야 이상없이 전송됨
        elapsed = elapsed + r.elapsed
        # escaping code for test
        # for debug
        # if count == 10:
        #     break
    print('End import. %d seconds elapsed.' % elapsed.second)

test_auth(email, passwd)
add_article(email, passwd, safaridb)
