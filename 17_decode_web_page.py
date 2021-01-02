import requests
from bs4 import BeautifulSoup


def decode_web(web_page):
    page = requests.get(web_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    # articles = soup.find_all('h2', class_="e1voiwgp0")
    articles = soup.select('h2.e1voiwgp0')
    return [t.get_text() for t in articles]


print(decode_web('https://www.nytimes.com/'))
