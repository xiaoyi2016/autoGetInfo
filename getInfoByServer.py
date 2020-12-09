# 先通过抓包软件对应用进行抓包分析， 找到对应的api，然后通过模拟请求，获取服务器返回的数据

# import urllib.request
import

#response = urllib.request.urlopen('https://api.douguo.net/personalized/home')
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))