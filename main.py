import base64
import io
import json
import re
import time
import urllib.request

import requests
import requests
from bs4 import BeautifulSoup
import requests
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import firestore
from firebase_admin import storage
from PIL import Image
import os
import random
import openpyxl
import pandas as pd
from pyautogui import size
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import shutil
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import time
import datetime
import pyautogui
import pyperclip
import csv
import sys
import os
import math
import requests
import re
import random
import chromedriver_autoinstaller
from PyQt5.QtWidgets import QWidget, QApplication, QTreeView, QFileSystemModel, QVBoxLayout, QPushButton, QInputDialog, \
    QLineEdit, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QCoreApplication
from selenium.webdriver import ActionChains
import numpy
import datetime
from window import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

def GetGangNam():

    print("지역 크롤링하기 시작")
    dataList=[]
    regions=['서울','경기|인천','대전|충청','대구|경북','부산|경남','광주|전라','강원도|제주']
    for region in regions:
        cookies = {
            'PHPSESSID': '4984k0pnhtiujtlof8d0981rv1',
            '_ga': 'GA1.1.451543972.1684079343',
            'hd_pops_15': '1',
            'e1192aefb64683cc97abb83c71057733': 'Y21w',
            '_ga_P9XZY1EJZ5': 'GS1.1.1684079343.1.1.1684079704.0.0.0',
        }

        headers = {
            'Accept': 'text/html, */*; q=0.01',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=4984k0pnhtiujtlof8d0981rv1; _ga=GA1.1.451543972.1684079343; hd_pops_15=1; e1192aefb64683cc97abb83c71057733=Y21w; _ga_P9XZY1EJZ5=GS1.1.1684079343.1.1.1684079704.0.0.0',
            'Referer': 'https://xn--939au0g4vj8sq.net/cp/?ca=20&loca_prt=%EC%84%9C%EC%9A%B8&local_1=%EC%A0%84%EC%B2%B4&local_2=%EC%84%9C%EC%9A%B8',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'ca': '20',
            'local_1': '전체',
            'local_2': region,
            'rpage': [
                '0',
                '0',
            ],
            'row_num': '5000',
        }

        response = requests.get(
            'https://xn--939au0g4vj8sq.net/theme/go/_list_cmp_tpl.php',
            params=params,
            cookies=cookies,
            headers=headers,
        )
        soup=BeautifulSoup(response.text,'lxml')
        liTags=soup.find_all('li',attrs={'class':'list_item'})
        for liTag in liTags:
            try:
                url="https://xn--939au0g4vj8sq.net"+liTag.find('a')['href']
            except:
                url=""
            # print('url:',url)

            # print(liTag)
            try:
                dday=liTag.find('span',attrs={'class':'dday'}).get_text()
                regex=re.compile("\d+")
                dday=regex.findall(dday)[0]
            except:
                dday="0"
            # print('dday:',dday)
            title=liTag.find('dt',attrs={'class':'tit'}).get_text()
            # print('title:',title)
            status=liTag.find('span',attrs={'class':'numb'}).get_text()
            regex=re.compile('신청 \d+')
            applyCount=regex.findall(status)[0].replace("신청","")
            regex = re.compile('모집 \d+')
            demandCount = regex.findall(status)[0].replace("모집","")
            # print('applyCount:',applyCount)
            # print('demandCount:',demandCount)
            if region=="강원|제주":
                region="기타"
            try:
                imageUrl=liTag.find('img',attrs={'class':'thumb_img'})['src']
                if imageUrl.find("https")<0:
                    imageUrl="https:"+imageUrl
            except:
                imageUrl=""
            regex=re.compile("id=\d+")
            myIndex=regex.findall(url)[0].replace("id=","")
            data={'platform':'강남맛집','region':region,'dday':dday,'title':title,'applyCount':applyCount,'demandCount':demandCount,'imageUrl':imageUrl,'url':url,'myImage':"강남맛집_"+myIndex}
            print(data)
            dataList.append(data)
        print("총갯수:",len(dataList))

    print("제품 크롤링하기 시작")
    cookies = {
        'PHPSESSID': '4984k0pnhtiujtlof8d0981rv1',
        '_ga': 'GA1.1.451543972.1684079343',
        'hd_pops_15': '1',
        'e1192aefb64683cc97abb83c71057733': 'Y21w',
        '_ga_P9XZY1EJZ5': 'GS1.1.1684079343.1.1.1684079704.0.0.0',
    }

    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # 'Cookie': 'PHPSESSID=4984k0pnhtiujtlof8d0981rv1; _ga=GA1.1.451543972.1684079343; hd_pops_15=1; e1192aefb64683cc97abb83c71057733=Y21w; _ga_P9XZY1EJZ5=GS1.1.1684079343.1.1.1684079704.0.0.0',
        'Referer': 'https://xn--939au0g4vj8sq.net/cp/?ca=20&loca_prt=%EC%84%9C%EC%9A%B8&local_1=%EC%A0%84%EC%B2%B4&local_2=%EC%84%9C%EC%9A%B8',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'ca': '30',
        'rpage': [
            '0',
            '0',
        ],
        'row_num': '5000',
    }

    response = requests.get(
        'https://xn--939au0g4vj8sq.net/theme/go/_list_cmp_tpl.php',
        params=params,
        cookies=cookies,
        headers=headers,
    )
    soup=BeautifulSoup(response.text,'lxml')
    liTags=soup.find_all('li',attrs={'class':'list_item'})
    for liTag in liTags:
        try:
            url="https://xn--939au0g4vj8sq.net"+liTag.find('a')['href']
        except:
            url=""
        # print('url:',url)

        # print(liTag)
        try:
            dday=liTag.find('span',attrs={'class':'dday'}).get_text()
            regex=re.compile("\d+")
            dday=regex.findall(dday)[0]
        except:
            dday="0"
        # print('dday:',dday)
        title=liTag.find('dt',attrs={'class':'tit'}).get_text()
        # print('title:',title)
        status=liTag.find('span',attrs={'class':'numb'}).get_text()
        regex=re.compile('신청 \d+')
        applyCount=regex.findall(status)[0].replace("신청","")
        regex = re.compile('모집 \d+')
        demandCount = regex.findall(status)[0].replace("모집","")
        # print('applyCount:',applyCount)
        # print('demandCount:',demandCount)
        # if region=="강원|제주":
        #     region="기타"
        region="기타"
        try:
            imageUrl=liTag.find('img',attrs={'class':'thumb_img'})['src']
            if imageUrl.find("https")<0:
                imageUrl="https:"+imageUrl
        except:
            imageUrl=""
        regex=re.compile("id=\d+")
        myIndex=regex.findall(url)[0].replace("id=","")
        data={'platform':'강남맛집','region':region,'dday':dday,'title':title,'applyCount':applyCount,'demandCount':demandCount,'imageUrl':imageUrl,'url':url,'myImage':"강남맛집_"+myIndex}
        print(data)
        dataList.append(data)
        print("총갯수:",len(dataList))


    return dataList
def GetNolowa():
    dataList=[]
    print("지역크롤링시작")
    page=1
    while True:
        cookies = {
            'PHPSESSID': 'sid67tsfqdbj2slve011j2bl73',
            '3dbe03ceb950cfecc3a0ba0538d4d0d6': 'MjExLjIxNS4xOTEuNzM%3D',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=sid67tsfqdbj2slve011j2bl73; 3dbe03ceb950cfecc3a0ba0538d4d0d6=MjExLjIxNS4xOTEuNzM%3D',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'category_id': '001',
            'sst': '',
            'sod': '',
            'page': str(page),
        }
        page=page+1
        response = requests.get('https://www.cometoplay.kr/item_list.php', params=params, cookies=cookies, headers=headers)
        soup=BeautifulSoup(response.text,'lxml')
        liGroup=soup.find('div',attrs={'class':'item_box_list'})
        lis=liGroup.find_all('li')
        if len(lis)==0:
            break
        for li in lis:
            url='https://www.cometoplay.kr/'+li.find('a')['href']
            title=li.find('span',attrs={'class':'it_name'}).get_text()
            # print('title:',title)
            dday=li.find('span',attrs={'class':'txt_num'}).get_text()
            regex=re.compile("\d+")
            dday=regex.findall(dday)[0]
            # print('dday:',dday)
            applyCount=li.find('b',attrs={'class':'txt_num point_color4'}).get_text()
            # print('applyCount:',applyCount)
            demandCount=li.find('b',attrs={'style':'color:#666;'}).get_text()
            # print('demandCount:',demandCount)
            imageUrl=li.find('img')['src'].replace('./','https://cometoplay.kr/')
            # print('imageUrl:',imageUrl)

            region="기타"
            if title.find('서울')>=0:
                region="서울"
            elif title.find('경기')>=0 or title.find('인천')>=0:
                region="경기|인천"
            elif title.find('대전')>=0 or title.find('충남')>=0 or title.find('충청')>=0 or title.find('충북')>=0:
                region="대전|충청"
            elif title.find('대구')>=0 or title.find('경북')>=0:
                region="대전|충청"
            elif title.find('부산')>=0 or title.find('경남')>=0:
                region="부산|경남"
            elif title.find('광주')>=0 or title.find('전남')>=0 or title.find('전북')>=0:
                region="광주|전라"

            regex=re.compile("it_id=\d+")
            myIndex=regex.findall(url)[0].replace("it_id=","")

            data = {'platform': '놀러와체험단', 'region': region, 'dday': dday, 'title': title, 'applyCount': applyCount,
                    'demandCount': demandCount, 'imageUrl': imageUrl,'url':url,'myImage':"놀러와체험단_"+myIndex}
            print(data)
            dataList.append(data)
        time.sleep(0.5)
        print("총갯수:", len(dataList))


    print("제품크롤링시작")
    page = 1
    while True:
        cookies = {
            'PHPSESSID': 'sid67tsfqdbj2slve011j2bl73',
            '3dbe03ceb950cfecc3a0ba0538d4d0d6': 'MjExLjIxNS4xOTEuNzM%3D',
        }
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            # 'Cookie': 'PHPSESSID=sid67tsfqdbj2slve011j2bl73; 3dbe03ceb950cfecc3a0ba0538d4d0d6=MjExLjIxNS4xOTEuNzM%3D',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }

        params = {
            'category_id': '002',
            'sst': '',
            'sod': '',
            'page': str(page),
        }
        page = page + 1
        response = requests.get('https://www.cometoplay.kr/item_list.php', params=params, cookies=cookies,
                                headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        liGroup = soup.find('div', attrs={'class': 'item_box_list'})
        lis = liGroup.find_all('li')
        if len(lis) == 0:
            break
        for li in lis:
            url = 'https://www.cometoplay.kr/' + li.find('a')['href']
            title = li.find('span', attrs={'class': 'it_name'}).get_text()
            # print('title:',title)
            dday = li.find('span', attrs={'class': 'txt_num'}).get_text()
            regex = re.compile("\d+")
            dday = regex.findall(dday)[0]
            # print('dday:',dday)
            applyCount = li.find('b', attrs={'class': 'txt_num point_color4'}).get_text()
            # print('applyCount:',applyCount)
            demandCount = li.find('b', attrs={'style': 'color:#666;'}).get_text()
            # print('demandCount:',demandCount)
            imageUrl = li.find('img')['src'].replace('./', 'https://cometoplay.kr/')
            # print('imageUrl:',imageUrl)

            region = "기타"
            # if title.find('서울') >= 0:
            #     region = "서울"
            # elif title.find('경기') >= 0 or title.find('인천') >= 0:
            #     region = "경기|인천"
            # elif title.find('대전') >= 0 or title.find('충남') >= 0 or title.find('충청') >= 0 or title.find('충북') >= 0:
            #     region = "대전|충청"
            # elif title.find('대구') >= 0 or title.find('경북') >= 0:
            #     region = "대전|충청"
            # elif title.find('부산') >= 0 or title.find('경남') >= 0:
            #     region = "부산|경남"
            # elif title.find('광주') >= 0 or title.find('전남') >= 0 or title.find('전북') >= 0:
            #     region = "광주|전라"

            regex = re.compile("it_id=\d+")
            myIndex = regex.findall(url)[0].replace("it_id=", "")

            data = {'platform': '놀러와체험단', 'region': region, 'dday': dday, 'title': title, 'applyCount': applyCount,
                    'demandCount': demandCount, 'imageUrl': imageUrl, 'url': url, 'myImage': "놀러와체험단_" + myIndex}
            print(data)
            dataList.append(data)
        time.sleep(0.5)
        print("총갯수:", len(dataList))
    return dataList
def GetDinnerQueen():
    dataList=[]

    page=1
    while True:
        cookies = {
            '_fbp': 'fb.1.1684080159081.1105236955',
            'PHPSESSID': '6e5437bafc8baedfdf62265e589e761a311dce4c',
            '_gid': 'GA1.2.1430089283.1684244645',
            '_gat_UA-58677533-2': '1',
            'wcs_bt': 'unknown:1684245532',
            '_ga_GFE876V0LZ': 'GS1.1.1684244621.3.1.1684245532.0.0.0',
            '_ga': 'GA1.1.668113333.1684080158',
        }

        headers = {
            'authority': 'dinnerqueen.net',
            'accept': '*/*',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'content-length': '0',
            # 'cookie': '_fbp=fb.1.1684080159081.1105236955; PHPSESSID=6e5437bafc8baedfdf62265e589e761a311dce4c; _gid=GA1.2.1430089283.1684244645; _gat_UA-58677533-2=1; wcs_bt=unknown:1684245532; _ga_GFE876V0LZ=GS1.1.1684244621.3.1.1684245532.0.0.0; _ga=GA1.1.668113333.1684080158',
            'origin': 'https://dinnerqueen.net',
            'referer': 'https://dinnerqueen.net/taste?ct=%EC%A7%80%EC%97%AD&lpage=3&query=&deal=&cate=&order=&area1=%EC%A0%84%EA%B5%AD&area2=%EC%A0%84%EC%B2%B4',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'ct': '지역',
            'area1': '전국',
            'area2': '전체',
            'page': str(page),
            'query': '',
        }
        page=page+1
        response = requests.post('https://dinnerqueen.net/taste/taste_list', params=params, cookies=cookies,
                                 headers=headers)
        try:
            result=json.loads(response.text)['layout']
        except:
            break
        soup=BeautifulSoup(result,'lxml')
        allTags=soup.find_all('div',attrs={'class':'qz-col pc2 lt3 tb2 mb2 mr-b8 mb-mr-b6'})
        isAllTags=len(allTags)
        if isAllTags==0:
            break
        for eachtag in allTags:
            url='https://dinnerqueen.net'+eachtag.find('a')['href']

            title=eachtag.find('p',attrs={'class':'qz-body-kr mb-qz-body2-kr ellipsis-2 color-title'}).get_text()
            # print('title:',title)
            try:
                dday=eachtag.find('p',attrs={'class':'qz-badge m layer-primary mr-b1 ver-t'}).get_text()
                dday=dday.replace("일 남음","").strip()
            except:
                dday=0
            # print('dday:',dday)
            applyCount=0
            demandCount=0
            imageUrl=eachtag.find('img')['src']
            # print('imageUrl:',imageUrl)

            region = "기타"
            if title.find('서울') >= 0:
                region = "서울"
            elif title.find('경기') >= 0 or title.find('인천') >= 0:
                region = "경기|인천"
            elif title.find('대전') >= 0 or title.find('충남') >= 0 or title.find('충청') >= 0 or title.find('충북') >= 0:
                region = "대전|충청"
            elif title.find('대구') >= 0 or title.find('경북') >= 0:
                region = "대전|충청"
            elif title.find('부산') >= 0 or title.find('경남') >= 0:
                region = "부산|경남"
            elif title.find('광주') >= 0 or title.find('전남') >= 0 or title.find('전북') >= 0:
                region = "광주|전라"



            regex=re.compile("/\d+")
            myIndex=regex.findall(url)[0].replace("/","")

            data = {'platform': '디너의여왕', 'region': region, 'dday': dday, 'title': title, 'applyCount': applyCount,
                    'demandCount': demandCount, 'imageUrl': imageUrl,'url':url,'myImage':"디너의여왕_"+myIndex}
            print(data)
            dataList.append(data)
        print("총갯수:", len(dataList))
        time.sleep(0.5)
    return dataList
def GetDailyView():
    print("지역크롤링")
    dataList=[]
    page=1
    while True:
        cookies = {
            'PHPSESSID': 'pq5but4qs6umog2cqtr2o4hci5',
            '3dbe03ceb950cfecc3a0ba0538d4d0d6': 'MjExLjIxNS4xOTEuNzM%3D',
        }

        headers = {
            'authority': 'www.dailyview.kr',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'PHPSESSID=pq5but4qs6umog2cqtr2o4hci5; 3dbe03ceb950cfecc3a0ba0538d4d0d6=MjExLjIxNS4xOTEuNzM%3D',
            'referer': 'https://www.dailyview.kr/item_list.php?category_id=001',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        params = {
            'category_id': '001',
            'sst': '',
            'sod': '',
            'page': str(page),
        }
        page=page+1
        response = requests.get('https://www.dailyview.kr/item_list.php', params=params, cookies=cookies,
                                headers=headers)


        soup=BeautifulSoup(response.text,'lxml')
        liGroup=soup.find('div',attrs={'class':'item_box_list'})
        lis=liGroup.find_all('li')
        if len(lis)==0:
            break
        for li in lis:
            url='https://dailyview.kr/'+li.find('a')['href']
            title=li.find('span',attrs={'class':'it_name'}).get_text()
            # print('title:',title)
            dday=li.find('span',attrs={'class':'txt_num'}).get_text()
            regex=re.compile("\d+")
            dday=regex.findall(dday)[0]
            # print('dday:',dday)
            applyCount=li.find('b',attrs={'class':'txt_num point_color4'}).get_text()
            # print('applyCount:',applyCount)
            demandCount=li.find('b',attrs={'style':'color:#666;'}).get_text()
            # print('demandCount:',demandCount)
            imageUrl=li.find('img')['src'].replace('./','https://dailyview.kr/')
            # print('imageUrl:',imageUrl)

            region="기타"
            if title.find('서울')>=0:
                region="서울"
            elif title.find('경기')>=0 or title.find('인천')>=0:
                region="경기|인천"
            elif title.find('대전')>=0 or title.find('충남')>=0 or title.find('충청')>=0 or title.find('충북')>=0:
                region="대전|충청"
            elif title.find('대구')>=0 or title.find('경북')>=0:
                region="대전|충청"
            elif title.find('부산')>=0 or title.find('경남')>=0:
                region="부산|경남"
            elif title.find('광주')>=0 or title.find('전남')>=0 or title.find('전북')>=0:
                region="광주|전라"
            regex=re.compile("it_id=\d+")
            myIndex=regex.findall(url)[0].replace("it_id=","")

            data = {'platform': '데일리뷰', 'region': region, 'dday': dday, 'title': title, 'applyCount': applyCount,
                    'demandCount': demandCount, 'imageUrl': imageUrl,'url':url,'myImage':"데일리뷰_"+myIndex}
            print(data)
            dataList.append(data)
        time.sleep(0.5)
        print("총갯수:", len(dataList))

    print("제품크롤링")
    page = 1
    while True:
        cookies = {
            'PHPSESSID': 'pq5but4qs6umog2cqtr2o4hci5',
            '3dbe03ceb950cfecc3a0ba0538d4d0d6': 'MjExLjIxNS4xOTEuNzM%3D',
        }

        headers = {
            'authority': 'www.dailyview.kr',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            # 'cookie': 'PHPSESSID=pq5but4qs6umog2cqtr2o4hci5; 3dbe03ceb950cfecc3a0ba0538d4d0d6=MjExLjIxNS4xOTEuNzM%3D',
            'referer': 'https://www.dailyview.kr/item_list.php?category_id=001',
            'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        }

        params = {
            'category_id': '002',
            'sst': '',
            'sod': '',
            'page': str(page),
        }
        page=page+1
        response = requests.get('https://www.dailyview.kr/item_list.php', params=params, cookies=cookies,
                                headers=headers)


        soup=BeautifulSoup(response.text,'lxml')
        liGroup=soup.find('div',attrs={'class':'item_box_list'})
        lis=liGroup.find_all('li')
        if len(lis)==0:
            break
        for li in lis:
            url='https://dailyview.kr/'+li.find('a')['href']
            title=li.find('span',attrs={'class':'it_name'}).get_text()
            # print('title:',title)
            dday=li.find('span',attrs={'class':'txt_num'}).get_text()
            regex=re.compile("\d+")
            dday=regex.findall(dday)[0]
            # print('dday:',dday)
            applyCount=li.find('b',attrs={'class':'txt_num point_color4'}).get_text()
            # print('applyCount:',applyCount)
            demandCount=li.find('b',attrs={'style':'color:#666;'}).get_text()
            # print('demandCount:',demandCount)
            imageUrl=li.find('img')['src'].replace('./','https://dailyview.kr/')
            # print('imageUrl:',imageUrl)

            region="기타"
            if title.find('서울')>=0:
                region="서울"
            elif title.find('경기')>=0 or title.find('인천')>=0:
                region="경기|인천"
            elif title.find('대전')>=0 or title.find('충남')>=0 or title.find('충청')>=0 or title.find('충북')>=0:
                region="대전|충청"
            elif title.find('대구')>=0 or title.find('경북')>=0:
                region="대전|충청"
            elif title.find('부산')>=0 or title.find('경남')>=0:
                region="부산|경남"
            elif title.find('광주')>=0 or title.find('전남')>=0 or title.find('전북')>=0:
                region="광주|전라"
            regex=re.compile("it_id=\d+")
            myIndex=regex.findall(url)[0].replace("it_id=","")

            data = {'platform': '데일리뷰', 'region': region, 'dday': dday, 'title': title, 'applyCount': applyCount,
                    'demandCount': demandCount, 'imageUrl': imageUrl,'url':url,'myImage':"데일리뷰_"+myIndex}
            print(data)
            dataList.append(data)
        time.sleep(0.5)
        print("총갯수:", len(dataList))

    return dataList
def SaveFirebaseDB(totalList):

    db = firebase_admin.db
    ref = db.reference()  # db 위치 지정, 기본 가장 상단을 가르킴
    ref.update({"data": totalList})
    print("저장완료")
def InitFirebase():
    cred = credentials.Certificate({
        "type": "service_account",
        "project_id": "experience-gen",
        "private_key_id": "6a967ec5eea30528f569dea9a04f3d136a6375cd",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC5gcn0Igb0HlUH\nF3af6eFWdJmynoUxJUVfBloJ/UUCWn4zLQUuUfd8r04L/wTYrV4CKcORJfl85T2/\nxSupVctXpg0Bzu4vDOB7eUEE7F68TSZVRKCMnimOft2QMlwljPbkG65dCJEMKRXL\nLb68oQ8Ko8epWkf5dWpnsrugajvRHriaoMXv6e8gVrZTCM4ShoJTqRZhot+u1goL\n8kRZuiS4nugZ/ezzWLVYMMaUYFavOkVvWcFvv4hmyu8FnmXGNi0hkGGWh8iLv7KH\n1keSdvcZVDk/mhqMKsz8e3gZazF1ovYYvdIOni8bdwB9YHJZo41pangWEXMglI8S\nZZ46IFf9AgMBAAECggEAEXvFWDhUxhvjEPYJ0hcti65q8JthcOOoXsUEe2iJYSgS\nONSHZnmHL73TR0IpEhrU1LNcS95zsxe6nXZXH8XcPPiDb/uGwJx1aRhhI7ZQqhfu\nAvSi2l3rC2kIN2zno7UIwoWcBgdRVFS9nxaX9sM0iGDYkoIrF7xp441u2Dbq8vx0\nbUAdj5mJEVvaOAtzr55EARxPEqL6zUttoHRzJ4pnTUKuVsJ69sibqua0pmwCurlF\n3PWNgnRs4PVX1NS4vs49WzMT6eb2eNp8+XuYeedDPItW/pfAf+y/rhVMsIHLlFBa\nkRzdxPTsTJM311TWgaiWiclp9Rld63FtVtAbBHzz6QKBgQDm/Mvs7DF5EfmhjP+D\ngNHaK6F+tsYE/XwYS0uDPncWbJ7CurRGQdB4XAd4odIHg7AVNmqSuwNDz3AH4dsG\nyGGQ3j3yq0rSYsUOWycVt6JSPZvyNuRDJxUiHWYbiFerpEe1kg9SMoMQXtsMsDFI\nR7VsBff1p3/efJcrMfHL1NClpwKBgQDNmDo/O6CrwtaCOUVJ//Rxzf7MWRK65+mr\naMEhX3ITiHUm1QtMuvHE+hLU4Ka+E9wsJqq4qqchXBr1v8ylHFJhIOdRSR5/MG1f\nLnTsRf51HsGNjQDsqAmqF0WLoU2ZZ0/b+MsBbaL7+GUPaNslRPJZi+agANjMZMwl\nq3OpwPbRuwKBgBAKSAL41+qnY+VjDC9Ol8QFuZ46BQA9tgtd1y2S/eQRwOiW3IPw\neBCTm3U2D4a0D1s5vybXU7+2vPnfJj2PVq8fr7+VQ4nej/6SN+GbMetyGc01IJ7F\nLQOEdR2+VxA1RUGHlgbIOS++1olIBvQU/rU0qOZnLkr97eVy/25/JcoLAoGALA6f\nDMXeXHBYP3e+XWk4HNsj6u57kQn5jP3ZxSkK7Ryk3jlxPnQhMzDTsEKj+L+QwvVW\nSFRplECEln0PgaJcFOxUJZshqefayDbQX4FwUfDRUWAR/qTTzVtHT/C1DFaTSnQ6\nLIguEQjdvzudGpN3y7CrL0Z/Lu26wafIFWyAd9kCgYBZTUrlgNmX0KEG0lwW+Gp4\nDRDrv5wwObfySKkez/g6Gm3IfUpBJuSyDZoAuTka4IKU4jybKWE16/qIpQth5u1Z\n9i4TzKDXODLgD//I1kDEl6H98fD2LPGjyIcQzAtsl9qVkjBRBZn/6KkKRkd8esZ9\n9vMIa4yP+R5BdznCBprR6A==\n-----END PRIVATE KEY-----\n",
        "client_email": "firebase-adminsdk-56cwd@experience-gen.iam.gserviceaccount.com",
        "client_id": "112011830418533229556",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-56cwd%40experience-gen.iam.gserviceaccount.com",
        "universe_domain": "googleapis.com",
    })
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://experience-gen-default-rtdb.asia-southeast1.firebasedatabase.app//',
        'storageBucket': 'experience-gen.appspot.com',
        # 'databaseURL' : '데이터 베이스 url'
    })

def SaveFirebaseStorage(fileName,firstFlag):
    # if firstFlag==True:


    # Put your local file path



    # refs=firebase_admin.storage.bucket().list_blobs()
    # for index,ref in enumerate(refs):
    #     print(index,print(type(ref)),ref)
    # # print(ref)


    # with open(fileName, "wb") as f:
    #     binaryImage=f.read()
    # binaryImage=base64.b64encode(binaryImage)
    # binaryImage=binaryImage.decode("UTF-8")
    #
    #
    #
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    blob.make_public()
    print("your file url", blob.public_url)



class Thread(QThread):
    cnt = 0
    user_signal = pyqtSignal(str)  # 사용자 정의 시그널 2 생성

    def __init__(self, parent,timeCycle):  # parent는 WndowClass에서 전달하는 self이다.(WidnowClass의 인스턴스)
        super().__init__(parent)
        self.parent = parent  # self.parent를 사용하여 WindowClass 위젯을 제어할 수 있다.
        self.timeCycle=timeCycle

    def run(self):
        print("222")

        timePrev=0
        InitFirebase()
        print("주기는:",self.timeCycle)
        while True:

            timeNow=datetime.datetime.now().timestamp()
            timeNowString = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

            if timeNow-timePrev>=60*self.timeCycle:
                timePrev=datetime.datetime.now().timestamp()
                text="크롤링 시작 / {}".format(timeNowString)
                self.user_signal.emit(text)
                dataList1 = GetGangNam()  # 강남맛집 검색
                text = "강남맛집 크롤링 완료"
                print(text)
                self.user_signal.emit(text)
                dataList2 = GetNolowa()  # 놀러와 검색
                text = "놀러와체험단 크롤링 완료"
                print(text)
                self.user_signal.emit(text)
                dataList3 = GetDinnerQueen()  # 디너의여왕 검색
                text = "디너의여왕 크롤링 완료"
                print(text)
                self.user_signal.emit(text)
                dataList4 = GetDailyView()  # 데일리뷰 검색
                text = "데일리뷰 크롤링 완료"
                print(text)
                self.user_signal.emit(text)
                totalList = dataList1 + dataList2 + dataList3 + dataList4  # 검색결과를 모두 합친다.


                with open('totalList.json', 'w') as f:
                    json.dump(totalList, f, indent=2)

                # =================JSON파일 읽어와서 올리기
                with open('totalList.json', "r") as f:
                    totalList = json.load(f)

                text = "전체 글 갯수:{}".format(len(totalList))
                print(text)
                self.user_signal.emit(text)
                firstFlag = True
                text = "그림 파일 저장중"
                print(text)
                self.user_signal.emit(text)
                for index, totalElem in enumerate(totalList):
                    # if index<=4635:
                    #     continue
                    filename = "{}.png".format(totalElem['myImage'])
                    print("{}번째 파일".format(index), filename)

                    if firstFlag == True:
                        # InitFirebaseStorage() #테스트에서만 켬
                        bucketList = storage.bucket().list_blobs()
                        preGetList = []
                        for bucketElem in bucketList:
                            # print('filename:',filename)
                            # print(str(bucketElem))
                            data = str(bucketElem)
                            preGetList.append(data)
                        # print('preGetList:', preGetList)
                        # print("그림갯수:", len(preGetList))
                        firstFlag = False
                    # print('filename:', filename)
                    skip_flag = False
                    for preGetElem in preGetList:
                        if preGetElem.find(filename) >= 0:
                            print("그림이미있음".format(filename))

                            skip_flag = True
                            break
                    if skip_flag == True:
                        continue

                    try:
                        headers = {
                            "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}
                        imageUrl = totalElem['imageUrl']
                        if imageUrl.find("no_img") >= 0 or len(imageUrl) == 0:
                            continue
                        print('{}번째 imageUrl:'.format(index), imageUrl)
                        image_res = requests.get(imageUrl, headers=headers)  # 그림파일 저장
                        image_res.raise_for_status()

                        with open(filename, "wb") as f:
                            f.write(image_res.content)  # 그림파일 각각 저장
                        text = "그림파일 저장중..."
                        print(text)
                        SaveFirebaseStorage(filename, firstFlag)

                        time.sleep(random.randint(8, 10) * 0.1)

                    except:
                        print("에러로건너뜀")
                        time.sleep(3)

                    print("=====================================")
                SaveFirebaseDB(totalList)
                text = "그림 파일 저장 완료"
                print(text)
                self.user_signal.emit(text)


            else:
                text="대기중..."
                self.user_signal.emit(text)
            time.sleep(10)
    def stop(self):
        pass

class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.path = "C:"
        self.index = None
        self.setupUi(self)
        self.setSlot()
        self.show()
        QApplication.processEvents()
        self.lineEdit.setText("60")
    def start(self):
        self.timeCycle=int(self.lineEdit.text())
        print('11')

        self.x = Thread(self,self.timeCycle)
        self.x.user_signal.connect(self.slot1)  # 사용자 정의 시그널2 슬롯 Connect
        self.x.start()

    def slot1(self, data1):  # 사용자 정의 시그널1에 connect된 function
        self.textEdit.append(str(data1))

    def setSlot(self):
        pass

    def setIndex(self, index):
        pass

    def quit(self):
        QCoreApplication.instance().quit()


app = QApplication([])
ex = Example()
sys.exit(app.exec_())