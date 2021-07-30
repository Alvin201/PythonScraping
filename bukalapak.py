import requests
import csv
import json
from bs4 import BeautifulSoup

key = input('Masukkan keyword : ')
write = csv.writer(open('results/{}.csv'.format(key), 'w', newline=''))
header = ['Nama', 'Harga']
write.writerow(header)

url = 'https://api.bukalapak.com/category-suggestions/categories?term={}&limit=5&access_token=u2U6cjiERyB-dC_3H_RusxjOEKZ06Lzm6q2z6QKIb3qwSQ'.format(key)

for page in range(1,11):
        parameter = {
        'prambanan_override': True,
        'keywords': key,
        'limit': 50,
        'offset': 50,
        'page': page,
        'facet': True,
        'access_token': 'mQGhy8j1LozcmzGrAl2hte7gSRlxqbY6LaHDpDZGRRMFbQ'
        }
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

        r = requests.get(url, params=parameter, headers=headers).json()
        #print(r.status_code)
        products = r['data']

        #collect product info
        for p in products:
                nama = p['id']
                harga = p['score']
                # stok = p['stock']
                # rating = p['rating']['average_rate']
                # kondisi = p['condition']
                # deskripsi = BeautifulSoup(p['description']).get_text()
                # kategori = p['category']['structure']
                # rilis = p['relisted_at']
                # kota = p['store']['address']['city']
                # provinsi = p['store']['address']['province']
                write = csv.writer(open('results/{}.csv'.format(key), 'a', newline=''))
                # data = [nama, harga, stok, rating, kondisi, deskripsi, kategori, rilis, kota, provinsi]
                data = [nama, harga]
                write.writerow(data)
