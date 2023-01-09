#!/bin/python3

# default mode: automatically run every 75s, and script must be on all the time
# cron mode: comment @repeater(line 77), and then run it in crontab on 5min basis (suggested)
#            If you want to run it every 75s in crontab, my suggestion is to write a shell code
#            that run this script 4 times every five minutes in cron, the shell script should be
#            same idea of the repeater I wrote here.
# the output file has a format as below:
# Year-Month-Day Hour:Minute:Second >>> view dm like coin collect share

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import time

# change the url here, this is only for BiliBili videos
link = "https://www.bilibili.com/video/BV1fY4y1F7GL?vd_source=bb34772c9c0cfb635943b6692a649ba0"


def request(url):
    try:
        html = requests.get(url=url, timeout=(3.05, 6.05))
        bs = BeautifulSoup(html.text, 'html.parser')
        if html.status_code == 404:
            return False
        else:
            return bs
    except requests.exceptions.ConnectionError:
        write("provided link is invalid")
    except Exception as error:
        write(error)


def analyze(full):
    general = list(full.find_all('span', class_='info-text'))
    data = []
    for each in general:
        element = re.findall(r'>(.+)<', str(each))[0]
        data.append(convert(element))

    extra = str(full.find_all('span'))
    dm = str(re.findall(r'历史累计弹幕数(\d+)', extra)[0])
    view = str(re.findall(r'总播放数(\d+)', extra)[0])

    result = f'{view} {dm} {data[0]} {data[1]} {data[2]} {data[3]}'
    return result


def convert(number):
    number = str(number)
    if '万' in number:
        new_num = int(float(number.strip('万')) * 10000)
    else:
        new_num = number
    return str(new_num)


def write(output):
    with open('data.txt', 'a') as file:
        now = datetime.now().strftime('%F %H:%M:%S')
        file.write(f'{now} >>> {output}\n')


def repeater(func):
    def wrapper():
        while True:
            start = time.time()
            func()
            end = time.time()
            time.sleep(75-(end-start))
    return wrapper


# comment this single line if you need
@repeater
def main():
    content = request(link)
    if content is False:
        write('video no longer exist in BiliBili')
    elif content is None:
        pass
    else:
        try:
            info = analyze(content)
            write(info)
        except Exception as analyze_error:
            write(analyze_error)


if __name__ == '__main__':
    main()
