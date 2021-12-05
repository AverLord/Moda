import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
quotes = soup.find_all('span', class_ = 'text')
authors = soup.find_all('small', class_ = 'author')
data = {}
for i in range(len(quotes)):
    data[authors[i].text]=quotes[i].text
print(data)

with open('result.json', 'w', encoding = 'utf-8') as file:
    json.dump(data, file)