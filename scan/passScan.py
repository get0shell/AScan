# @Author : alan
# @File : passScan.py
import paramiko
import threading
import ftplib
from impacket import smb
import pymysql


def sshScan(t, i, o, u, p):
    try:
        t.acquire()
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname=i, port=o, username=str(u), password=str(p), timeout=10)
        print('[+]SSH连接成功，用户：%s,密码：%s' % (u, p))
        client.close()
    except:
        t.release()


def ssh():
    with open('./plug/passdict/username.txt', 'r')as f:
        user = f.readlines()
    with open('./plug/passdict/password.txt', 'r')as f:
        passw = f.readlines()
    ip = input("请输入IP：").strip()
    port = input("请输入端口：").strip()
    s = threading.Semaphore(10)
    for i in user:
        username = i.strip()
        for j in passw:
            password = j.strip()
            t = threading.Thread(target=sshScan, args=(s, ip, port, username, password))
            t.start()


def ftp_anyScan(t, i, o):
    try:
        t.acquire()
        ftp = ftplib.FTP()
        ftp.connect(i, o, 2)
        ftp.login()
        ftp.quit()
        print('[+]FTP连接成功，无用户名密码')
    except:
        t.release()


def ftp_any():
    ip = input("请输入IP：").strip()
    port = input("请输入端口：").strip()
    s = threading.Semaphore(10)
    t = threading.Thread(target=ftp_anyScan, args=(s, ip, port))
    t.start()


def ftpScan(t, i, o, u, p):
    try:
        t.acquire()
        ftp = ftplib.FTP()
        ftp.connect(i, o, 2)
        ftp.login(u, p)
        ftp.quit()
        print('[+]FTP连接成功，用户：%s,密码：%s' % (u, p))
    except:
        t.release()


def ftp():
    with open('./plug/passdict/username.txt', 'r')as f:
        user = f.readlines()
    with open('./plug/passdict/password.txt', 'r')as f:
        passw = f.readlines()
    ip = input("请输入IP：").strip()
    port = input("请输入端口：").strip()
    s = threading.Semaphore(10)
    for i in user:
        username = i.strip()
        for j in passw:
            password = j.strip()
            t = threading.Thread(target=ftpScan, args=(s, ip, port, username, password))
            t.start()


def smbScan(t, i, u, p):
    try:
        t.acquire()
        c = smb.SMB('*SMBSERVER', i)
        c.login(u, p)
        print('[+]SMB连接成功，用户：%s,密码：%s' % (u, p))
    except:
        t.release()


def smb():
    with open('./plug/passdict/username.txt', 'r')as f:
        user = f.readlines()
    with open('./plug/passdict/password.txt', 'r')as f:
        passw = f.readlines()
    ip = input("请输入IP：").strip()
    s = threading.Semaphore(10)
    for i in user:
        username = i.strip()
        for j in passw:
            password = j.strip()
            t = threading.Thread(target=smbScan, args=(s, ip, username, password))
            t.start()


def mysqlScan(t, i, u, p):
    try:
        t.acquire()
        db = pymysql.connect(host=i, user=u, password=p)
        print('[+]MYSQL连接成功，用户：%s,密码：%s' % (u, p))
        db.close()
    except:
        t.release()


def mysql():
    with open('./plug/passdict/username.txt', 'r')as f:
        user = f.readlines()
    with open('./plug/passdict/password.txt', 'r')as f:
        passw = f.readlines()
    ip = input("请输入IP：").strip()
    s = threading.Semaphore(10)
    for i in user:
        username = i.strip()
        for j in passw:
            password = j.strip()
            t = threading.Thread(target=mysqlScan, args=(s, ip, username, password))
            t.start()


def passScan():
    print('''
    支持弱口令扫描类型：
    1、SSH弱口令扫描
    2、FTP弱口令扫描
    3、SMB弱口令扫描
    4、MYSQL弱口令扫描
    ''')
    m = input("请选择扫描的类型：").strip()
    if m == '1':
        ssh()
    elif m == '2':
        ftp()
        ftp_any()
    elif m == '3':
        smb()
    elif m == '4':
        mysql()
    else:
        print('请输入正确的参数')
