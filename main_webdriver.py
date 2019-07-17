#coding:utf-8
__author__ = 'Kuangen Zhang'
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
import signal

username_str = "****" # 你的校园网登陆用户名
password_str = "****" # 你的校园网登陆密码

can_connect = True


def login():
    try:
        driver = webdriver.Firefox()
        driver.get("http://net.********.edu.cn") # 你的校园网登陆地址
        time.sleep(3)
        username_input = driver.find_element_by_id("uname") # 校园网登陆用户名的输入控件ID, 浏览器上右键查看网页源代码查询
        password_input = driver.find_element_by_id("pass") # 校园网登陆密码的输入控件ID, 浏览器上右键查看网页源代码查询
        print('Searching connect')
        login_button = driver.find_element_by_id("connect") # 校园网登陆连接的点击控件ID, 浏览器上右键查看网页源代码查询
        print('Find connect successfully')
        username_input.send_keys(username_str)
        password_input.send_keys(password_str)
        print('Input user info')
        login_button.click()
        print('Connect')
    except:
        print(getCurrentTime(), u"登陆函数异常")
    finally:
        driver.close()


#获取当前时间
def getCurrentTime():
    return time.strftime('[%Y-%m-%d %H:%M:%S]',time.localtime(time.time()))


#判断当前是否可以连网
def handler(signum, frame):
    try:
        global can_connect
        can_connect = False # 默认判断连接为失败状态
        # 需要设置timeout是因为断网时request会堵住程序, 设置timeout后最多等待10s，如果没有request成功, can_connect为False
        baidu_request=requests.get("http://www.baidu.com", timeout = 10)
        if(baidu_request.status_code==200):
            baidu_request.encoding = 'utf-8'
            baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
            baidu_input = baidu_request_bsObj.find(value="百度一下")
            if baidu_input==None:
                return False
            can_connect = True # 只有可以request 到百度的网址，并且页面中含有“百度一下”这几个字符，才判断连接成功
            return True
        else:
            print('Offline')
            return False
    except:
        print ('error')
        return False


#主函数
def main():
    print (getCurrentTime(), u"Hi，校园网自动登陆脚本正在运行")
    while True:
        while True:
            start_time = time.time()
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(10)
            end_time = time.time()
            print(end_time - start_time)
            global can_connect
            print(can_connect)
            if not can_connect:
                print (getCurrentTime(),u"断网了...")
                try:
                    login()
                except:
                    print(getCurrentTime(), u"浏览器出了bug")
            else:
                print (getCurrentTime(), u"一切正常...")
                time.sleep(5)
            time.sleep(10)
        time.sleep(10)


main()
