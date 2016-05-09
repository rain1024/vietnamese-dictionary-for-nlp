import requests
import json

__author__ = 'LanAnh'
import re

with open("../data/VV/vv30K.dict") as text_file:
    content = text_file.read()
    result = re.findall("(^@.*$)", content, re.MULTILINE)
    result = result[3:]
    length = len(result)
    for index, text in enumerate(result):
        text = text[1:]
        print "{}/{}: {}".format(index + 1, length, text)
        url = "http://192.168.99.100:8000/api/words/"
        data = {'name': text, 'type': 'a'}
        headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json'}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        pass
