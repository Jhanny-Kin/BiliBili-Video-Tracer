#!/bin/python3

# Because this is a manual version, there is no exception protection.
# If nothing goes wrong here, it works for sure in the auto version.

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time

# change the url here, this is only for BiliBili videos
link = "https://www.bilibili.com/video/BV1fY4y1F7GL?vd_source=bb34772c9c0cfb635943b6692a649ba0"


def request(url):
    html = requests.get(url=url, timeout=(3.05, 6.05))
    bs = BeautifulSoup(html.text, 'html.parser')
    return bs


def analyze(full):
    title = re.findall(r'>(.+)<', str(full.find_all('h1', class_='video-title tit')))[0]

    general = list(full.find_all('span', class_='info-text'))
    data = []
    for each in general:
        element = re.findall(r'>(.+)<', str(each))[0]
        data.append(convert(element))

    extra = str(full.find_all('span'))
    like = str(re.findall(r'点赞数(\d+)', extra)[0])
    dm = str(re.findall(r'历史累计弹幕数(\d+)', extra)[0])
    view = str(re.findall(r'总播放数(\d+)', extra)[0])

    result = [title, like, dm, view] + data[1:]
    return result


def convert(number):
    number = str(number)
    if '万' in number:
        new_num = int(float(number.strip('万')) * 10000)
    else:
        new_num = number
    return str(new_num)


def decorator(func):
    def wrapper():
        print('-' * 40)
        print(f'Time: {datetime.now()}')
        start = time.time()
        func()
        stop = time.time()
        print(f'Program finished in {(stop-start):.2f}s')
        print('-' * 40)
    return wrapper


def printing(output):
    print()
    print(f'Title: {output[0]}')
    print(f'Views: {output[1]}')
    print(f'DM: {output[2]}')
    print(f'Likes: {output[3]}')
    print(f'Coins: {output[4]}')
    print(f'Collects: {output[5]}')
    print(f'Shares: {output[6]}')
    print()


@decorator
def process():
    content = request(link)
    info = analyze(content)
    printing(info)


if __name__ == '__main__':
    process()
