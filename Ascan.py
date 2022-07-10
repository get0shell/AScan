# @Author : alan
# @File : Ascan.py

from scan import subScan,dirScan,vulScan
from scan import passScan

def Ascan():
    print('============================================欢迎使用AScan==============================================')
    print('''
            =                 ==                ==                   =                ==          =
           =  =           =       =          =        =             =  =              =  =        =
          =    =            ==             =                       =    =             =    =      =
         = =  = =                ==        =                      = =  = =            =      =    =
        =        =        =       =          =        =          =        =           =        =  =
       =          =           ==                ==              =          =          =          ==
    ''')
    print('=====================================================================================================')
    print('''
    扫描模块：
    1、子域名扫描
    2、目录扫描
    3、漏洞扫描
    4、弱口令扫描
    请选择对应的序号进行扫描
    ''')
    t = input('请输入对应扫描模式序号：').strip()
    if t == '1':
        subScan.subScan()
    elif t == '2':
        dirScan.dirScan()
    elif t == '3':
        vulScan.vulScan()
    elif t == '4':
        passScan.passScan()
    else:
        print('参数错误！')


if __name__ == '__main__':
    Ascan()
