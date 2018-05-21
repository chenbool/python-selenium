# -*- coding: utf-8 -*-  
from selenium import webdriver 
from time import sleep

class Qzone(object):
	def __init__(self,qq,password,content):
		self.qq=qq
		self.password=password
		self.content = content
		#后缀
		self.suffix = " --from python3.6"

	def login(self):
		self.driver = webdriver.Chrome()
		self.driver.maximize_window()
		self.driver.get("http://i.qq.com")
		self.driver.switch_to_frame("login_frame")
		self.driver.find_element_by_id("switcher_plogin").click()
		#账号
		self.driver.find_element_by_id("u").clear()
		self.driver.find_element_by_id("u").send_keys(self.qq)
		#密码
		self.driver.find_element_by_id("p").clear()
		self.driver.find_element_by_id("p").send_keys(self.password)
		#登录
		self.driver.find_element_by_id("login_button").click()
		print('login is ok')
		sleep(4)
		self.run()

	def run(self):
		# 打开个人
		self.driver.find_element_by_id("aIcenter").click()
		sleep(3)
		self.driver.find_element_by_id("checkin_button").click()
		sleep(2)
		# 定位输入信息frame  
		self.driver.switch_to_frame("checkin_likeTipsFrame")
		sleep(2)

		#天气签到
		self.driver.find_element_by_xpath(".//*[@id='idMainStampList']/li[1]").click()
		sleep(1)
		content = "return document.getElementsByClassName('c_tx2')[0].innerHTML='%s %s' " %(self.content,self.suffix)
		self.driver.execute_script(content)
		# 发布
		self.driver.find_element_by_id("idEditorPublishBtn").click()

		#截图保存
		self.driver.save_screenshot( "./screenshot/%s.png" %(self.qq) )

		sleep(2)
		#退出窗口
		self.driver.quit()


# def main():  
# 	qzone = Qzone('30524165','123456','发布测试')
# 	qzone.login()
  
# if __name__ == "__main__":  
# 	main()  
