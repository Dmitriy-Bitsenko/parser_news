from django.shortcuts import render
from bs4 import BeautifulSoup
import requests


lenta = 'https://lenta.ru/'
rbc = 'https://www.rbc.ru/'
russia_today = 'https://russian.rt.com/'


lenta_list = []


def get_lenta():

    lent = requests.get(lenta).text
    soup = BeautifulSoup(lent, 'lxml')
    posts = soup.find_all('a', class_="card-mini _topnews")
    for post in posts:
        title = post.find(class_='card-mini__title').text
        url = post.get('href')
        data = {'title': title,
                'url': 'https://lenta.ru' + url}
        lenta_list.append(data)


get_lenta()


rbc_list = []


def get_rbc():
    rb = requests.get(rbc).text
    soup = BeautifulSoup(rb, 'lxml')
    posts = soup.find_all('div', class_='main__feed js-main-reload-item')
    for post in posts:
        title = post.find(class_='main__feed__title-wrap').text
        url = post.find('a').get('href')
        data = {'title': title,
                'url': url}
        rbc_list.append(data)


get_rbc()


rt_list = []


def get_rt():
    rt = requests.get(russia_today).text
    soup = BeautifulSoup(rt, 'lxml')
    posts = soup.find_all(class_='card__heading card__heading_main-news')
    for post in posts:
        title = post.find(class_='link link_color').text
        url = post.find('a').get('href')
        data = {'title': title,
                'url': 'https://russian.rt.com' + url}
        rt_list.append(data)


get_rt()


def main_page(requests):
    context = {
        'lenta_list': lenta_list,
        'rbc_list': rbc_list,
        'rt_list': rt_list,
    }
    return render(requests, 'news_app/main_page.html', context)


def weather():
    pass


# print(rt_list, rbc_list, lenta_list)
