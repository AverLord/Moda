import requests
from bs4 import BeautifulSoup
import json

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('h4', class_ = 'card-title')
authors = soup.find_all('h5')
data = {}
for i in range(len(quotes)):
    data[quotes[i].text]=authors[i].text
print(data)

with open('result1.json', 'w', encoding = 'utf-8') as file:
    json.dump(data, file)