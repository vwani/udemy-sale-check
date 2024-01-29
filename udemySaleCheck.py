from bs4 import BeautifulSoup
import requests
import lxml
import re
from win11toast import toast

data = requests.get('https://www.udemy.com/')

soup = BeautifulSoup(data.content, features='lxml')

for script in soup(["script", "style"]):
    script.extract()

text = soup.find_all('p')
content = ''
for t in text:
    content += t.get_text()

    

if (a:=re.findall(r'[\w\s\d]+₹4\d{2}[\s\.,!]|[\w\s\d]+\b(?:Sale)\b[\w\s\d]+',content, re.IGNORECASE)):
    toast('Udemy Sale Today!', f'{'. '.join(map(lambda x: x.strip().rstrip("."), a))}. Click to open Udemy', on_click='https://www.udemy.com', button='Dismiss')

else:
    print(False)
