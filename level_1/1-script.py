#!/usr/bin/python3
"""1-script module"""
import requests
from bs4 import BeautifulSoup


url = "http://158.69.76.135/level1.php"

for i in range(4096):
    session = requests.Session()
    auth = session.get(url).text
    soup = BeautifulSoup(auth, 'html.parser')
    key = soup.find(type="hidden")['value']
    data = {'id': "4281", 'holdthedoor': "submit", 'key': key}
    session.post(url, data=data)
