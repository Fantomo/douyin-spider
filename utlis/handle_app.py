# -*- encoding: utf-8 -*-

from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


class Element:
	SKIP_AD_BTN = (By.ID, 'com.ss.android.ugc.aweme:id/cu')  # 跳过广告按钮
	INDEX_SEARCH_BTN = (By.ID, 'com.ss.android.ugc.aweme:id/av9')  # 主页搜索
	INPUT_BOX = (By.ID, 'com.ss.android.ugc.aweme:id/a93')  # 搜索框
	SEARCH_BTN = (By.ID, 'com.ss.android.ugc.aweme:id/d90')  # 搜索按钮
	USER_BTN = (By.ID, 'android:id/text1')  # 导航栏用户按钮
	USER = (By.ID, 'com.ss.android.ugc.aweme:id/b3q')  # 选择用户
	FANS_NUM = (By.ID, 'com.ss.android.ugc.aweme:id/aee')  # 粉丝数


class HandleApp:

	def __init__(self):

		desired_caps = {
			'platformName': 'Android',
			# 'platformVersion': '5.1.1',
			# 'deviceName': '127.0.0.1:62001',
			'platformVersion': '7.1.1',
			'deviceName': '3e18d75a',
			'appPackage': 'com.ss.android.ugc.aweme',
			'appActivity': '.splash.SplashActivity',
			'noReset': True,
			'unicodeKeyboard': True,
			'resetKeyboard': True
		}
		appium_server = "http://localhost:4723/wd/hub"
		# appium_server = "http://192.168.3.23:4723/wd/hub"
		self.driver = webdriver.Remote(appium_server, desired_caps)
		self.e = Element()

	def get_size(self):
		"""
		:return: 手机页面大小 
		"""
		x = self.driver.get_window_size()['width']
		y = self.driver.get_window_size()['height']
		return x, y

	def input_user_id(self, user_id, flag=None):
		try:
			# 检查是否有广告
			WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.e.SKIP_AD_BTN)).click()
		except TimeoutException:
			pass
		# 主页搜索
		WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.e.INDEX_SEARCH_BTN)).click()
		# 输入用户id
		WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.e.INPUT_BOX)).send_keys(user_id)
		# 搜索用户按钮
		WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.e.SEARCH_BTN)).click()
		# 用户按钮
		WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.e.USER_BTN))[2].click()
		# 进入用户主页
		WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.e.USER))[0].click()

		if flag == 'fans':
			"""
			判断用户是否有粉丝
			:param user: 用户id
			"""
			fans = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.e.FANS_NUM))
			if fans.text != '0':
				fans.click()

	def move_page(self):
		"""
		移动应用页面
		"""
		x, y = self.get_size()
		x *= 0.5
		y1 = y * 0.9
		y2 = y * 0.15

		flag = True
		while flag:
			if "暂时没有更多了" in self.driver.page_source:
				flag = False
			else:
				self.driver.swipe(x, y1, x, y2)
				sleep(3)


if __name__ == "__main__":
	f = HandleApp()
	f.input_user_id("锅盖wer", 'fans')
	f.move_page()
