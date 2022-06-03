from bs4 import BeautifulSoup
import lxml
import requests
import re

url = 'https://lenta.ru/news/2022/06/01/proverka/'
requests.get(url)
otvet = requests.get(url).text  #то, что сервер присылает обратно в каечсвте ответа на запрос
print(otvet)

soup = BeautifulSoup(otvet, 'lxml')

zagolovok = soup.find(f'span', class_="topic-body__title")
print(zagolovok)

#g = f'[^<span class_="topic-body__title">].*[^</span>]'
#m = re.findall(g, zagolovok)
#print(m)

zagolovok = str(zagolovok)[32:-7]
print(zagolovok)