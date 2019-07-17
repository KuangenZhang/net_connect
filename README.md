# net_connect
校园网络自动重连

教程说明: https://zhuanlan.zhihu.com/p/74082157



* pip安装selenium包：
```
pip install selenium
```
* 下载webdriver firefox内核（python可以操控的浏览器，跟我们平时用的浏览器不同，代码中使用Firefox的driver），下载地址：
```
https://github.com/mozilla/geckodriver/releases
```

* 解压缩下载的文件到一个文件夹，如果是linux则复制到/usr/bin/geckodriver,  如果是windows则手动添加环境变量，这样python运行时可以找到这个driver。linux 复制该driver的代码：
```
sudo cp geckodriver /usr/bin/geckodriver
```

* 修改代码的校园网用户名，校园网密码，校园网登陆地址，校园网用户名输入控件ID，校园网密码输入控件ID，以及校园网连接控件ID。以上几个ID都可以通过查看网页源码得到。
```
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
```

* 运行代码：
```
python main_webdriver.py
```

* 接下来可以试试手动登出校园网，看看程序是否自动连接成功。

* References：http://blog.csdn.net/zcy0xy/article/details/78675334

