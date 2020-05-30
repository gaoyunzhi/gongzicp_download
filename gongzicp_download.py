#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cached_url
from bs4 import BeautifulSoup
import yaml

chapter_prefix = 'https://www.gongzicp.com/novel/getChapterList?nid='

def getNid(url):
	return url.split('-')[-1].split('.')[0]

def download(url):
	nid = getNid(url)
	content = cached_url.get(chapter_prefix + nid)
	print(content)
	content = yaml.load(content, Loader=yaml.FullLoader)
	print(content)

	
if __name__ == "__main__":
	download('https://www.gongzicp.com/novel-168140.html')