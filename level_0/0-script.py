#!/usr/bin/python3
"""0-script module"""
import requests


url = "http://158.69.76.135/level0.php"
data = {'id': "4281", 'holdthedoor': "submit"}

for i in range(1024):
    requests.post(url, data=data)
