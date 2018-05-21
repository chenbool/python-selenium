# -*- coding: utf-8 -*-  
from selenium import webdriver 
from time import sleep

class Tieba(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password
	def login(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("https://tieba.baidu.com/index.html")

		# 点击登陆
		self.driver.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
		sleep(1)
		self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__footerULoginBtn"]').click()
		sleep(1)
		# username
		self.driver.find_element_by_id('TANGRAM__PSP_10__userName').clear()
		self.driver.find_element_by_id('TANGRAM__PSP_10__userName').send_keys(self.username)
		self.driver.find_element_by_id('TANGRAM__PSP_10__password').clear()
		self.driver.find_element_by_id('TANGRAM__PSP_10__password').send_keys(self.password)
		# 登陆
		self.driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
		sleep(4)
		self.run()

	def run(self):
		# div#onekey_sign>a是一键签到的css选择器
		self.driver.find_element_by_css_selector("div#onekey_sign>a").click()
		self.driver.find_element_by_css_selector(".j_sign_btn ").click()

		self.driver.save_screenshot( "./screenshot/%s.png" %(self.username) )

		sleep(3)
		#退出窗口
		self.driver.quit()

# def main():  
# 	tieba = Tieba('81001989@qq.com','s123')
# 	tieba.login()
  
# if __name__ == "__main__":  
# 	main()  
