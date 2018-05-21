# -*- coding: utf-8 -*-  
from selenium import webdriver 
from time import sleep

class MeiTuan(object):
	def __init__(self, phone):
		self.phone = phone
		self.coupon = [
			'25B2AAEB95004BC4BF452F49BE7A9F48',
			'D76086C4D5724CA3804ECFA8602601D4',
			'6082EA3FF5C24E23A04492A7B192CEAD',
			'D855C7B3CCB74A189C07CE6B33B1BD02', # 美团支付
			'14E548DE17D74C2F955ACEED6EC46BD9',
			'9C3B5EDD443D46D8B3D660EE28BD7641',
			'27CE9DAA94FB44DD9BB86743E0604B09',
			'0DE7C95E01B442DBA629DEDBEA6FCE8B',
			'5C0CA32F1E8F4C4ABB75866B2047719A',

		]

	def run(self):
		self.driver = webdriver.Chrome()
		self.driver.set_window_size(480,840)
		self.driver.get('https://github.com/bool1993')

		for v in self.coupon:
			self.send(v)
			print(v)

		sleep(2)
		self.driver.quit()

	def send(self,v):

		url = 'https://activity.waimai.meituan.com/coupon/h5channel/'
		# 打开新窗口
		newwindow = 'window.open("'+url+v+'");'
		self.driver.execute_script(newwindow)
		 
		# 切换到新的窗口
		handles = self.driver.window_handles
		self.driver.switch_to_window(handles[-1])

		sleep(1.5)
		# phone
		self.driver.find_element_by_xpath('//*[@id="phone-input"]').clear()
		self.driver.find_element_by_xpath('//*[@id="phone-input"]').send_keys(self.phone)
		# 领取
		self.driver.find_element_by_xpath('//*[@id="capture-btn"]').click()

		print('-------------------------------------------------------')
		sleep(1.5)
		self.driver.close()
		self.driver.switch_to_window(handles[0]) 
		

def main():  
	mt = MeiTuan('13913714891')
	mt.run()
  
if __name__ == "__main__":  
	main()  