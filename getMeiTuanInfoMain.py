#-*- coding：utf-8 -*-

#################################
# purpose: 获取美团外卖商家的货物，销量，产品 等信息
# author: wan jie
# place: shanghai
# 基于 appium 方案
#################################

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# appium服务监听地址
server='http://localhost:4723/wd/hub'

# app启动参数
desired_caps={
 "platformName": "Android",
 "deviceName": "dandelion",
 "appPackage": "com.sankuai.meituan.takeoutnew",
 "appActivity": "com.sankuai.waimai.business.page.homepage.MainActivity"
}

def process():
    driver = webdriver.Remote(server,desired_caps)
    wait = WebDriverWait(driver,30)
    # 获取登录按钮
    try:
     adbtn = wait.until(EC.presence_of_element_located((By.ID,"com.sankuai.meituan.takeoutnew:id/close")))
     adbtn.click()
    except Exception:
        print('')


if __name__ == '__main__':
        print('获取美团外卖app的数据信息')
        process()