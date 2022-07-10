# @Author : alan
# @File : dirScan.py

import requests
def scan():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    url = input('请输入url：').strip()
    with open('./plug/dir.txt', 'rt', encoding='utf-8') as f:
        m = f.readlines()

        for i in m:
            Url = url + i
            response = requests.get(Url, headers=headers)
            if response.status_code == 200:
                print('[+]存在目录:' + i)
            else:
                pass


def scan1():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
    }
    pwd = input('请输入文件路径:').strip()
    with open(pwd, 'rt', encoding='utf-8') as f:
        m = f.readlines()
        for i in m:

            with open('./plug/dir.txt', 'rt', encoding='utf-8') as f:
                j = f.readlines()
                for h in j:
                    Url = str(i.strip('\n')) + str(h)
                    response = requests.get(Url, headers=headers)
                    if response.status_code == 200:
                        print('[+]存在目录:' + Url)
                    else:
                        pass


def dirScan():
    print('======================================================')
    print('参数规格:')
    print('1、单个域名扫描')
    print('2、多域名文件扫描')
    print('域名格式:http://www.xxx.com')
    print('======================================================')
    t = input('请输入扫描模式:').strip()
    if t == '1':
        scan()
    elif t == '2':
        scan1()
    else:
        print('参数错误！')
