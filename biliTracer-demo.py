#!/bin/python3

import requests
from bs4 import BeautifulSoup
import re
import time
import datetime

# change your target video url from BiliBili below
url = "https://www.bilibili.com/video/BV1fY4y1F7GL?spm_id_from=333.999.0.0&vd_source=bb34772c9c0cfb635943b6692a649ba0"
headers = {
	# change the agency if you want, it seems to be unnecessary when this script is created
	"User-Agent": "I am NOT a Python Spyder",
}


# a simple decorator just for interface
def decorator(func):
	def wrapper():
		print('-' * 40)
		start = time.time()
		func()
		stop = time.time()
		print(f'Program finished in {(stop-start):.2f}s')
		print('-' * 40)
	return wrapper


# convert the chinese number expression into a universal way
def convert(data_list: list):
	converted_list = []
	for item in data_list:
		item = str(item)

		if '万' in item:
			new_item = int(float(item.strip('万')) * 10000)
		else:
			new_item = item

		converted_list.append(str(new_item))
	return converted_list


# give a label for each data gathered, and put them into a dictionary
def visualize(result_list):
	output_dict = {}
	index_keys = ['Views', 'DM', 'Likes', 'Coins', 'collect', 'Share']

	for num in range(0, 6):
		output_dict[index_keys[num]] = result_list[num]

	return output_dict


@decorator
def analyze():
	# request for the html webpage
	html = requests.get(url=url, headers=headers).text
	now = datetime.datetime.now()  # get current time

	bs = BeautifulSoup(html, 'html.parser')  # convert to bs

	title = re.findall(r'>(.+)<', str(bs.find_all('h1', class_='video-title tit')))[0]  # get video title

	# get video information of the video
	information = list(bs.find_all('span', class_='info-text'))
	data = []
	for each in information:
		element = re.findall(r'>(.+)<', str(each))[0]
		data.append(element)

	# get some extras
	dm = re.findall(r'历史累计弹幕数(\d+)', html)[0]
	times = re.findall(r'总播放数(\d+)', html)[0]

	# arrange all data gathered
	result = [times, dm] + convert(data)
	output = visualize(result)

	# printing out
	print(f'Title: {title}')
	print(f'Time: {now}')
	print()
	for key, value in output.items():
		print(f'{key}: {value}')
	print()


if __name__ == '__main__':
	try:
		analyze()
	except Exception as error:
		print(error)
