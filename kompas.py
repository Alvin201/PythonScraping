from datetime import date
import requests
import csv
from bs4 import BeautifulSoup


class switch(object):
        def __init__(self, value):
                self.value = value
                self.fall = False

        def __iter__(self):
                """Return the match method once, then stop"""
                yield self.match
                raise StopIteration

        def match(self, *args):
                """Indicate whether or not to enter a case suite"""
                if self.fall or not args:
                        return True
                elif self.value in args:  # changed for v1.5, see below
                        self.fall = True
                        return True
                else:
                        return False

headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'id,en-US;q=0.7,en;q=0.3',
        'Host' : 'indeks.kompas.com',
        'Referer' : 'https://news.kompas.com/',
        'Connection' : 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
        }


def kompas():
    datas = []
    r = requests.get(url, headers=headers)
    #print(r.url)
    #print(r.status_code)
    soup = BeautifulSoup(r.text, 'html.parser')
    #print(soup)
    items = soup.findAll('div', 'article__list clearfix')
    #print(items)
    for it in items:
        try : nm = ''.join(it.find('h3', 'article__title article__title--medium').text.strip().split('\n'))
        except : nm = ''
        print(nm)
        datas.append([nm])

    for d in datas:
        if any(field.strip() for field in d):  # remove blank rows
            try:
                writer.writerow(d)
            except: ''

print("Select site")
print("1. News")
print("2. Nasional")

#day = date.today()
site = int(input('Enter a site : '))
pagein = int(input('Enter a page : '))
year = int(input('Enter a year : '))
month = int(input('Enter a month : '))
day = int(input('Enter a day : '))
date1 = date(year, month, day)

# for i in range(pagein):
#     i += 1
#     url = 'https://indeks.kompas.com/?site=news&date={}&page={}'.format(date1, i)
#     print(url)
#     kompas()

 head = ['Name']
 with open('results/{}.csv'.format(site), 'w', newline='') as out:
      writer = csv.writer(out,delimiter=',')     
      writer.writerow(head)

for case in switch(site):
#     head = ['Name']
#     writer = csv.writer(open('results/{}.csv'.format(site), 'w', newline=''))
#     writer.writerow(head)
    if case(1):
        for i in range(pagein):
            i += 1
            url = 'https://indeks.kompas.com/?site=news&date={}&page={}'.format(date1, i)
            print(url)
            kompas()
        print('Export Successfully')
        break
    if case(2):
        for i in range(pagein):
            i += 1
            url = 'https://indeks.kompas.com/?site=nasional&date={}&page={}'.format(date1, i)
            print(url)
            kompas()
        print('Export Successfully')
        break
    if case():
        print ("something else!")
        break
