#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cached_url
from bs4 import BeautifulSoup
import yaml

chapter_prefix = 'https://www.gongzicp.com/novel/getChapterList?nid='

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
	for cid in getIds(content):
		print(cid)
	

	
if __name__ == "__main__":
	download('https://www.gongzicp.com/novel-168140.html')