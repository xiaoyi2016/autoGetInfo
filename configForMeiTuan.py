# 非共性部分的内容，通过配置文件来设置。 方便代码可以复用实现不同app信息的抓取

# 1 手机相关配置
# 1.1 手机的serial no 用于adb连接
PHONE_SERIAL_NO = '1234567890ABCDEF'


# 2 app 相关配置
# 2.1 启动activity配置
APP_LAUNCH_CMD = 'am start -n com.sankuai.meituan.takeoutnew/.ui.page.boot.WelcomeActivity'
