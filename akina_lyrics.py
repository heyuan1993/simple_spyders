# -*- coding: utf-8 -*-
"""
Created on Sun 02 04 23:25:30 2017

@author: heyua_000
This spyder is for getting lyrics from funsite of Nakamori Akina
Because this is a simple funsite, special techniques are not needed here.
Base webpage:
http://live.music.coocan.jp/review/list_cd_title_by_composition.htm
"""
spyder_type = 2 
# 1 for static page for composer imformation



import requests
from bs4 import BeautifulSoup
import re,time
import os,json
import base64
from Crypto.Cipher import AES
from pprint import pprint


import os
import numpy as np
import scipy.io as sio

import pandas as pd
from pandas import Series, DataFrame, ExcelWriter


import matplotlib.pyplot as plt

#导入结巴分词库(分词)
import jieba as jb
#导入结巴分词(关键词提取)
import jieba.analyse


work_path = 'D:\\Python_learning\\Project_6_akina_lyrics'
os.chdir(work_path)

if spyder_type ==1 :
    # orginal page = target page
    # keyword 中森明菜，search for all video less than 10 min and arrange by danmu numbers
    root_url = 'http://live.music.coocan.jp/review/list_cd_title_by_composition.htm'
    add_url  = ''
elif spyder_type ==2 :
    # original page: http://space.bilibili.com/32419811/#!/channel-detail/831/1/0
    # ajax page    : http://space.bilibili.com/ajax/channel/getVideo?mid=32419811&cid=831&p=1&num=30&order=0
    if   spyder_type ==2 :
        # 从频道中获取数据
        root_url = 'http://live.music.coocan.jp/review-cgi/utahime_lyrics.cgi?compo='
        add_url  = ''

_session = requests.session()
# _session.headers.update(headers_url)


if spyder_type ==2 :
    #############################for type 1###############################
    #html=bytes([])
    for pageCount in range(396,468):
        #pageCount = pageCount+1
        pageUrl = root_url + str(pageCount) + add_url
        #pageUrl = 'http://search.bilibili.com/all?keyword=%E4%B8%AD%E6%A3%AE%E6%98%8E%E8%8F%9C&page=1&order=click&tids_1=3&tids_2=29'
        r = requests.get(url=pageUrl)
        html = r.content.decode()
        #对抓取的页面进行编码
        title = re.findall(r'<TD align="center"><FONT style="font-size: 15pt">(.*?)</FONT></TD>',html)[0]
        composers = re.findall(r'<TD><FONT style="font-size: 13pt">(.*?)</FONT></TD>',html)
        lyrics_composer = '作詞：' + re.sub(r'<br>', r'&',composers[0]) + '\n' 
        music_composer  = '作曲：' + re.sub(r'<br>', r'&',composers[1]) + '\n' + '\n' + '\n'
        lyrics_content  = re.findall(r'<TD align="center"><FONT style="font-size:12pt;line-height:125%;">(.*?)</FONT></TD>',html)
        lyrics_content  = re.sub(r'<br>', r'\n',lyrics_content[0]) 
        file_name = str(pageCount) + '_' + title

        bib_files = open(file_name,'w', encoding='utf8')
        bib_files.write(title + '\n')
        bib_files.write(lyrics_composer)
        bib_files.write(music_composer)
        bib_files.write(lyrics_content)

        bib_files.close()

        #response = requests.get(pageUrl)
        #soup = BeautifulSoup(response.text)
        print(pageUrl)
