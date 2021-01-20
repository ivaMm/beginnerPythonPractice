import requests
from bs4 import BeautifulSoup


def decode_web(web_page):
    page = requests.get(web_page)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.select('h1.content-header__row.content-header__hed')
    print_it(title)
    write_it(title, 'w')
    header = soup.select('div.content-header__row.content-header__dek')
    print_it(header)
    write_it(header, 'a')
    author = soup.select('div.content-header__row.content-header__byline p')
    print_it(author)
    write_it(author, 'a')
    articles = soup.select('.article__chunks p')
    print_it(articles)
    write_it(articles, 'a')


def print_it(my_text):
    for t in my_text:
        print(t.get_text() + '\n')


def write_it(my_text, wa):
    with open('monica.txt', wa) as f:
        for t in my_text:
            f.write(t.get_text() + '\n')


decode_web('http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture')
