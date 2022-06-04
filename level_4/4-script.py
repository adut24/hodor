#!/usr/bin/python3
"""4-script module"""
import requests
from bs4 import BeautifulSoup


url = "http://158.69.76.135/level4.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0)'
           + ' Gecko/20100101 Firefox/100.0', 'referer': url}
prox_url = "https://free-proxy-list.net/"
i = 0

while i < 98:
    session = requests.Session()
    prox_cont = session.get(prox_url).text
    prox_soup = BeautifulSoup(prox_cont, 'html.parser')
    prox_ips = prox_soup.find('tbody').find_all('tr')
    for ip in prox_ips:
        try:
            proxies = {'http': 'http://' + str(ip.find('td').text)}
            auth = session.get(url, headers=headers).text
            soup = BeautifulSoup(auth, 'html.parser')
            key = soup.find(type="hidden")['value']
            data = {'id': "4281", 'holdthedoor': "submit", 'key': key}
            session.post(url, data=data, headers=headers, proxies=proxies,
                         timeout=5)
            check = list(soup.find_all('td'))
            for a in range(len(check)):
                if '4281' in check[a].text:
                    break
            if i < int(check[a + 1].text):
                i = int(check[a + 1].text)
                print(f'{i}')
            else:
                print('vote fail')
        except Exception:
            print("proxy fail")
