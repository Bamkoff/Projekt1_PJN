import requests
from bs4 import BeautifulSoup
import re
import sys
import time

def get_review(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    reviews = soup.find('div', id="reviewsList")
    if reviews is not None:
        marks = reviews.find_all('span', class_='big-number')
        review = reviews.find_all('p', class_="p-expanded js-expanded mb-0")
        if marks is not None and review is not None and len(marks) == len(reviews):
            with open('data/reviews2', 'a', encoding='utf-8', errors='ignore') as file:
                for i in range(len(marks)):
                    file.write(marks[i].text.replace(' ', '').replace('\n', '') + review[i].text.replace('\n', '') + '\n')
            file.close()

for i in range(118):
    page = requests.get('https://lubimyczytac.pl/katalog/' + str(i+1))
    soup = BeautifulSoup(page.content, 'html.parser')
    links = soup.find_all('a', class_="authorAllBooks__singleTextTitle float-left")
    for link in links:
        time.sleep(2)
        href = re.search(r'href=\"([^"]+)\"', str(link))
        get_review('https://lubimyczytac.pl' + href.group(1).replace(' ',''))