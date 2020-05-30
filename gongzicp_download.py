#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cached_url
from bs4 import BeautifulSoup
import yaml
import time
import os

chapter_prefix = 'https://www.gongzicp.com/novel/getChapterList?nid='
detail_prefix = 'https://www.gongzicp.com/read-%s.html'
content_anchor = 'content: "'
novel_anchor = 'novelName: "'

def getNid(url):
	return url.split('-')[-1].split('.')[0]

def getIds(content):
	for item in content['data']['list']:
		cid = item.get('id')
		if cid:
			yield cid

def download(url):
	nid = getNid(url)
	content = cached_url.get(chapter_prefix + nid)
	content = yaml.load(content, Loader=yaml.FullLoader)
	novel_name = None
	for cid in getIds(content):
		raw_content = cached_url.get(detail_prefix % cid)
		raw_content = raw_content
		content = raw_content.split(content_anchor)[1].split('",')[0]
		if not novel_name:
			novel_name = raw_content.split(novel_anchor)[1].split('",')[0]
			novel_name = novel_name.encode().decode('unicode-escape')
			os.system('mkdir download > /dev/null 2>&1')
			os.system('rm download/%s.txt > /dev/null 2>&1' % novel_name)
		content = content.replace('\/', '/')
		soup = BeautifulSoup(content, 'html.parser')
		for item in soup.find_all('p', class_='cp-hidden'):
			item.decompose()
		with open('download/%s.txt' % novel_name, 'a') as f:
			f.write(soup.text.encode().decode('unicode-escape'))
		time.sleep(1)
		return
	
if __name__ == "__main__":
	download('https://www.gongzicp.com/novel-168140.html')