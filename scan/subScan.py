# @Author : alan
# @File : subScan.py

import requests
import threading

def run(e,s):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0",
    }
    s.acquire()
    with open('./plug/sub.txt', 'rt', encoding='utf-8') as f:
        m = f.readlines()
        for i in m:
            url = 'http://' + str(i.strip('\n')) + '.' + str(e)

            try:
                response = requests.get(url, headers=header)

                if response.status_code == 200:
                    print('[-]存在域名:' + str(i.strip('\n')) + '.' + str(e))
                else:
                    pass
            except requests.exceptions.ConnectionError:
                requests.status_codes = 'xxx'


def subScan():
    print('======================================================')
    print('域名格式:xxx.com')
    print('======================================================')
    domain = input('请输入域名：').strip()
    mutex = threading.Lock()
    for i in range(5):
        t = threading.Thread(target=run,args=(domain,mutex))
        t.start()