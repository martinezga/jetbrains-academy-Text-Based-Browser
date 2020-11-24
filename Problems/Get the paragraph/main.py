import re

import requests

from bs4 import BeautifulSoup

word = input()
url = input()

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')

all_paragraphs = soup.find_all('p')
for paragraph in all_paragraphs:
    find_word = paragraph.find(string=re.compile(word))
    if find_word:
        print(paragraph.text)
