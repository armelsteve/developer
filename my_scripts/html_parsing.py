from bs4 import BeautifulSoup
import requests

with open('file.html') as file:
    soup = BeautifulSoup(file, 'lxml')
    content = soup.find_all('p')
    for i in content:
        del i 
        print(i)