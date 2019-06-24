# 抖音爬虫

### 项目环境
* python3  
* requests
* appium
* selenium

### 步骤

``` python
# appium 配置参数
desired_caps = {
            'platformName': 'Android',  # 手机系统
            'platformVersion': '5.1.1',  # 系统版本
            'deviceName': '127.0.0.1:62001',  # 设备名
            'appPackage': 'com.ss.android.ugc.aweme',  # app包名
            'appActivity': '.splash.SplashActivity',
            'noReset': True,  # 在当前session前不重置app状态
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }
```

1. [获取app的package和Activity.](https://github.com/Fantomo/Python-FAQ/blob/master/%E8%8E%B7%E5%8F%96apk%E7%9A%84packageName%E5%92%8CActivity.md)
2. 使用uiautomatorviewer 做App 元素定位
3. 使用Appium 做自动滑动用户视频页与fans页
4. 导入项目依赖 pip install -r requirements.txt
5. 使用mitmdump 做数据解析 将视频数据存入redis(简单去重), fans数据存入mongo
```python
# 先启动 mitmdump 监听数据
mitmdump -s[script] -p[port]
python run_video_spider.py
# 再启动自动化脚本
python handle_app.py
# 下载redis 中的视频 
python download_video.py
```

~~~
Tips:手机代理 mitmdump ip地址和端口
~~~
