import requests
import csv
from datetime import datetime
import json
from bs4 import BeautifulSoup


format_date = datetime.today().strftime('%Y-%m-%d')
write = csv.writer(open('results/' + format_date + '.csv', 'w', newline=''))
header = ['Category','Name','Couriers']
write.writerow(header)


#token = 'XL4rBkxW7VPPBX48ghCXzlCOp5Ze-7gF90u2k_BZU5ygSw'
token = input('Input Token : ')
url_token = 'https://api.bukalapak.com/couriers/categories?access_token={}'.format(str(token))

headers = {
        'Accept' : 'application/json, text/plain, */*',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'id,en-US;q=0.7,en;q=0.3',
        'Referer' : 'https://www.bukalapak.com/',
        'Origin' : 'https://www.bukalapak.com/',
        'Host' : 'api.bukalapak.com',
        'Connection' : 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
        }

r = requests.get(url_token, headers=headers).json()
#r = requests.get(url, params=parameter, headers=headers)
#print(r.status_code)

products = r['data']
#print(products)
count = 0
for a in products:
    category = a['category']
    name = a['name']
    couriers = a['couriers']
    #print(a['name'])
    count+=1
    strcouriers = str(couriers).replace("[","").replace("'","").replace("]","").replace('"',"")
    print('No.: ',count,'Category: ',category, 'Name :',name, 'Couriers :',strcouriers)
    write = csv.writer(open('results/' + format_date + '.csv', 'a', newline=''))
    data = [category,name,strcouriers]
    write.writerow(data)