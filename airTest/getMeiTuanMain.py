# 获取美团外卖平台上的商家，产品 等信息
# 基于 airtest 方案

from airtest.core.api import *
from poco.exceptions import PocoNoSuchNodeException
from airtest.core.android.adb import ADB
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from configForMeiTuan import *

def clickElement(img):
    try:
        if not img.exists():
            img.click()
    except PocoNoSuchNodeException:
        pass

def MainProcess():
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    auto_setup(__file__)

    adb = ADB(serialno=PHONE_SERIAL_NO)

    # 点亮屏幕
    adb.start_shell('input keyevent 26')

   # 按比例滑动屏幕解锁
    print(poco.get_screen_size())
    xy = poco.get_screen_size()
    x = xy[0]
    y = xy[1]
    swipe((0.5 * x, 0.6 * y), (0.5 * x, 0.3 * y), duration=1)

    # 开启美团外卖应用
    adb.start_shell(APP_LAUNCH_CMD)

    # img = poco(text="美团外卖")
    #clickElement(img)

    img = poco(resourceId="com.sankuai.meituan.takeoutnew:id/close")
    clickElement(img)

    img = poco(text="美食")
    clickElement(img)

    #img = poco("com.sankuai.meituan.takeoutnew:id/list_item_view").child("com.sankuai.meituan.takeoutnew:id/textview_poi_name ")
    img = poco(text="华莱士·全鸡汉堡（古美店）")

    try:
        if not img.exists():
            print('元素找到')
            img.click()
    except PocoNoSuchNodeException:
        pass

if __name__ == '__main__':
        print('获取美团外卖app的数据信息')
        MainProcess()