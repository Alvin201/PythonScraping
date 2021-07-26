import requests
import csv
from bs4 import BeautifulSoup

n = input('please enter the term : ')
url = 'https://www.tokopedia.com/search?st=product&q={}'.format(n)

headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'id,en-US;q=0.7,en;q=0.3',
        'Host' : 'www.tokopedia.com',
        'Connection' : 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
        }
datas = [] #variabel list

#r = requests.get(url_token, headers=headers).json()
r = requests.get(url, headers=headers)
#print(r.status_code)
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup)
items = soup.findAll('div', 'css-12sieg3')
for it in items:
        try : nm_shoes = ''.join(it.find('div', {'data-testid':'spnSRPProdName'}).text.strip().split('\n'))
        except : nm_shoes = ''
        try : price_shoes = ''.join(it.find('div', {'data-testid':'spnSRPProdPrice'}).text.strip().split('\n'))
        except : price_shoes = ''
        print(nm_shoes,price_shoes)
        datas.append([nm_shoes,price_shoes])

head = ['Name', 'Price']
writer = csv.writer(open('results/{}.csv'.format(n), 'w', newline=''))
writer.writerow(head)
for d in datas: writer.writerow(d)

print('Export Successfully')