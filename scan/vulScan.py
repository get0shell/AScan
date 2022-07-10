# @Author : alan
# @File : vulScan.py

import json
import os
import threading

import requests
import re


def run(u, i):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    }
    i.acquire()
    pathDir = os.listdir('./plug/vul/')
    for allDir in pathDir:
        p = os.path.join('./plug/vul/' + allDir)
        try:
            with open(p, 'rt', encoding='utf-8') as f:
                json_data = json.load(f)
                url = u + json_data['payload']
                response = requests.get(url, headers=header)
                i = re.search(json_data['res'], response.text)
                if i:
                    print('[+] 存在漏洞：' + json_data['name'])
        except Exception:
            print('请求异常，检查url是否正确')


def vulScan():
    print('url格式：http://www.xxx.com/ OR http://www.xxx.com/?id=')
    domain = input('请输入域名：').strip()
    mutex = threading.Lock()
    for i in range(1):
        t = threading.Thread(target=run, args=(domain, mutex))
        t.start()
