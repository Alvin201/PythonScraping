import requests
import csv
from bs4 import BeautifulSoup


n = input('please enter the term : ')
p = int(input('please enter the page : '))
#url = 'https://www.tokopedia.com/search?st=product&q={}'.format(n)
# url = 'https://www.tokopedia.com/search?navsource=home&page={}&q={}'.format(p,n)
headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Accept-Language' : 'id,en-US;q=0.7,en;q=0.3',
        'Host' : 'www.tokopedia.com',
        'Connection' : 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
        }
datas = []
count_page = 0
for i in range(p):
        i += 1
        url = 'https://www.tokopedia.com/search?navsource=home&page={}&q={}&st=product'.format(i, n)
        print(url)
        #r = requests.get(url_token, headers=headers).json()
        r = requests.get(url, headers=headers)
        # print(r.url)
        soup = BeautifulSoup(r.text, 'html.parser')
        #print(soup)
        items = soup.find_all('div', {'class': 'css-12sieg3'})
        for it in items:
            try :
                nm = ''.join(it.find('div', {'data-testid':'spnSRPProdName'}).text.strip().split('\n'))
            except : nm = ''

            try :
                price = ''.join(it.find('div', {'data-testid':'spnSRPProdPrice'}).text.strip().split('\n'))
            except : price = ''

            #shop locator and shop name in 1 div
            data = [d.find_all('span') for d in it.find_all('div', {'class': 'css-1rn0irl'})]
            temp = []
            value = ""
            test = ""
            for i in data:
                for j in i:
                    temp.append(j.text)
                    a = ' '.join(str(x) for x in temp)
                    print(a)

            try:
                rating = ''.join(it.find('span','css-etd83i').text.strip().split('\n'))
            except:
                rating = ''

            try:
                sold = ''.join(it.find('span', 'css-1kgbcz0').text.strip().split('\n')).replace('Terjual','')
            except:
                sold = ''

            print(nm.replace("!",''),price,a,rating,sold)
            datas.append([nm.replace("!",''),price,a,rating,sold])

head = ['Name', 'Price','Shop Loc','Rating','Sold']
writer = csv.writer(open('results/{}.csv'.format(n), 'w', newline=''))
writer.writerow(head)
with open('results/{}.csv'.format(n), 'w', newline='') as out:
    writer = csv.writer(out, delimiter='|')
    writer.writerow(head)
    for d in datas:
        if any(field.strip() for field in d):  # remove blank rows
            try:
                writer.writerow(d)
            except: ''
    print('Export Successfully')

