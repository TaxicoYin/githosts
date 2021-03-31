#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import os
import subprocess

class gitip:
    def __init__(self, ip_list):
        super().__init__()
        self.ip_list = ip_list
        self.header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
        self.ip_1 = 'https://github.com.ipaddress.com/' # github.com
        self.ip_2 = 'https://github.com.ipaddress.com/gist.github.com' # gist.github.com
        self.ip_3 = 'https://github.com.ipaddress.com/assets-cdn.github.com' # assets-cdn.github.com
        self.ip_4 = 'https://githubusercontent.com.ipaddress.com/raw.githubusercontent.com' # raw.githubusercontent.com
        self.ip_5 = 'https://github.com.ipaddress.com/api.github.com'
        self.ip_6 = 'https://fastly.net.ipaddress.com/github.global.ssl.fastly.net'
    def get_1(self): # github.com
        response = requests.get(self.ip_1, headers = self.header)
        soup = BeautifulSoup(response.text, features = 'lxml')
        self.ip_list.append(soup.find_all('ul', {'class': 'comma-separated'})[0].text + '    github.com')
    def get_5(self): 
        response = requests.get(self.ip_5, headers = self.header)
        soup = BeautifulSoup(response.text, features = 'lxml')
        self.ip_list.append(soup.find_all('ul', {'class': 'comma-separated'})[0].text + '    api.github.com')
    def get_6(self): 
        response = requests.get(self.ip_6, headers = self.header)
        soup = BeautifulSoup(response.text, features = 'lxml')
        self.ip_list.append(soup.find_all('ul', {'class': 'comma-separated'})[0].text + '    github.global.ssl.fastly.net')
    def get_2(self):
        response = requests.get(self.ip_2, headers = self.header)
        soup = BeautifulSoup(response.text, features = 'lxml')
        self.ip_list.append(soup.find_all('ul', {'class': 'comma-separated'})[0].text + '    gist.github.com')
    def get_3(self):
        response = requests.get(self.ip_3, headers = self.header)
        soup = BeautifulSoup(response.text, features = 'lxml')
        ips = soup.find_all('li')
        for i in range(4):
            self.ip_list.append(ips[i].text + '    assets-cdn.github.com')
    def get_4(self):
        response = requests.get(self.ip_4, headers = self.header)
        soup = BeautifulSoup(response.text, features = 'lxml')
        ip = soup.find_all('ul', {'class': 'comma-separated'})[0].text
        lip=int(len(ip)/4)
        ip=ip[0:lip]
        
        #curadress > p:nth-child(1) > a
        #curadress > p:nth-child(2) > a
        self.ip_list.append(ip + '    raw.githubusercontent.com')
        self.ip_list.append(ip + '    gist.githubusercontent.com')
        self.ip_list.append(ip + '    gitst.githubusercontent.com')
        self.ip_list.append(ip + '    cloud.githubusercontent.com')
        self.ip_list.append(ip + '    camo.githubusercontent.com')
        self.ip_list.append(ip + '    avatars0.githubusercontent.com')
        self.ip_list.append(ip + '    avatars1.githubusercontent.com')
        self.ip_list.append(ip + '    avatars2.githubusercontent.com')
        self.ip_list.append(ip + '    avatars3.githubusercontent.com')
        self.ip_list.append(ip + '    avatars4.githubusercontent.com')
        self.ip_list.append(ip + '    avatars5.githubusercontent.com')
        self.ip_list.append(ip + '    avatars6.githubusercontent.com')
        self.ip_list.append(ip + '    avatars7.githubusercontent.com')
        self.ip_list.append(ip + '    avatars8.githubusercontent.com')
        

if __name__ == '__main__':
    ip_list = []
    error = 0
    github = gitip(ip_list)
    try:
        github.get_1()
    except:
        print('github.com 申请出错')
        error+=1
    try:
        github.get_2()
    except:
        print('gist.github.com 申请出错')
        error+=1
    try:
        github.get_3()
    except:
        print('assets-cdn.github.com 申请出错')
        error+=1
    try:
        github.get_5()
    except:
        print('api.github.com 申请出错')
        error+=1
    try:
        github.get_6()
    except:
        print('github.global.ssl.fastly.net 申请出错')
        error+=1
    try:
        github.get_4()
    except:
        print('raw.githubusercontent.com 申请出错')
        error+=1
    # print(github.ip_list)
    if error == 0:
        for i in github.ip_list:
            print(i)
