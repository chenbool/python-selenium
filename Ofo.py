# -*- coding: utf-8 -*-  
from selenium import webdriver 
from time import sleep

class Ofo(object):
	def __init__(self, phone):
		self.phone = phone
		# https://www.looquan.com/lu-view-id-2839.html
		self.coupon = [
			'15184304287456',
			'15184306730207',
			'15184303705070',
			'15202925423706', # 亲子幼教网
			'338471516862866673', #到温江
			'15183606773736',	#唐山
			'15183607395593',	#唐山
			'15183607993869',
			'213231515766515926', #民生银行
			'213231515766438835', #民生银行
			# '15197273070172', 
			# '15196295593004', #沈煜伦
			# '15196295115667', #沈煜伦
			# '15196294569979', 
			# '15197885424058', #林依晨
			# '213231516183477815', #58同城
			# '213231516183581440', #58同城
			# '338471515486154717', #建设银行
			# '338401517218600364', #泓华医疗
			# '338401517218687227', #泓华医疗
			# '15194422318556', #牛子潘
			# '15194422021970', #牛子潘
			# '15194421756826', #牛子潘
			# '15175632878276', #王老吉
			# '213231515738717533', #oppo
			# '213231515738660435', #oppo
			# '213231515492643108', #微商银行
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

		url = 'http://ofo-campaign.ofo.com/slots/index.html#/?activityId='
		# 打开新窗口
		newwindow = 'window.open("'+url+v+'");'
		self.driver.execute_script(newwindow)
		 
		# 切换到新的窗口
		handles = self.driver.window_handles
		self.driver.switch_to_window(handles[-1])

		sleep(2)

		# 领取 
		self.driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[4]/button').click()

		# 检测是否存在
		try:
		    res = self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div/div[2]/div/input')
		except:
		    pass
		else:
			res.send_keys(self.phone)
			self.driver.find_element_by_xpath('//*[@id="app"]/div/div[4]/div/div/div/div[4]/div/button').click()

		print('-----------------------ok--------------------------------')
		sleep(5)
		self.driver.close()
		self.driver.switch_to_window(handles[0]) 
		

def main():  
	ofo = Ofo('13913714891')
	ofo.run()
  
if __name__ == "__main__":  
	main()  