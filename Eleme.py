# -*- coding: utf-8 -*-  
from selenium import webdriver 
from time import sleep

class Eleme(object):
	def __init__(self, phone):
		self.phone = phone
		self.coupon = [
			'c68029a7131bde003d5413cf31950c1f&a', #优惠券1 萨普科技
			'd3f6ef29396084213d4aa2a2ee841ff8&b', #优惠券2 邮政储存
			'd3f6ef29396084213d4aa2a2ee841ff8&b', #优惠券3 50元新人
			'7050e9455f9bc76df1674cf586d511cb&c', #优惠券4 超有利
			'b47945459feba3ac2e05cb902306fbd1&',  #优惠券5 超市
			'e2232327baba89cf29168622c52c5875&',  #优惠券6 元宵喜乐会
			# '42683367a9403fa8940e28cfaf55ded6&a', #oppo r11s
			# '6f1469f55b26ee6607fc15c6daab238e&c',  #淘票票
			# '1beb3f8c1615621fa857633e2fe5396e&c',  #星小班
			# '1f19f566cdf0d5e1525d7854c75351ce&b',  #百事可乐
			# '572788129478a22df8115e13a4f9fa1c&c',  #一起好
			# '83a1493798b62d034756400542d45319&b',  #上线了
			# 'ccd5115bb86144d4e832a5d630f17b5e&b',  #张新发
			# '4a2f8e9de66cf6025b3e51d0531890fa&a',  #中国移动 和多号
			# 'fb9c8138788f5e04263b2b583ce06209&b',  #城铁东城
			# '6156464e881de089b2b98eec2c7a6961&b',  #世联空间
			# 'e1d6395937baf42cc965af8a25ce13d5&b',  #创可贴
			# '8c00eada0afb518ff1dee9136e41f4c7&',  #腊月小镇
			# 'c8d3df2c7cea26890c35889c2bf4ef7a&a',  #vivo
			# '004dc92069c7bdd4f446c2a9371c3dbf&c',  #秒推新联盟
			# '69d82df716a14481c179cba532e7e2de&b',  #菜根科技
			# '648ba29ade30052d1fb3d558f5f784b3&b',  #创造与魔法
			# '39173251ba0aacc94d96269b0e2b0ed2&a',  #天玑汇富
			# '994f5871082bcb29387550e844cad964&b',  #OK学车
			# 'f3d9c5a3c28170b5035dd8232ae17fb2&c',  #苏宁易购
			# '0a75a4b3c141032e3591e93d65847049&a',  #国信证券
			# '42625ddeebc02b5c6b65b095f430fc93',  #滴滴快车
			# 'df0b100215ca8a7d0a78b1693d1ef8d9',  #哈罗单车
			# 'a8728512ead0a7783e517360f9d45b07',  #创园国际
			# '3363c80ffd892e54a1b5b9ce1742c590&',  #美的地产
			# 'a79ad6ebf17898905d9c22c066fe923b&a',  #龙券网
			# 'fcd086daaeba3936ce0429288073711e',  #速易递
			# 'f54cdac59fc562ad4e0a399ee7bc2d07',  #top
			# 'd644bdd975e4c6990da56494f760f58f',  #爱动漫
			# '2dc53685bf44424ae84b16107f810034',  #爱奇艺
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

		url = 'https://h5.ele.me/baida/#group_sn='
		# 打开新窗口
		newwindow = 'window.open("'+url+v+'");'
		self.driver.execute_script(newwindow)
		 
		# 切换到新的窗口
		handles = self.driver.window_handles
		self.driver.switch_to_window(handles[-1])

		sleep(1.5)
		# phone
		self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/input').clear()
		self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/input').send_keys(self.phone)
		# 领取
		self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/button').click()

		print('-------------------------------------------------------')
		sleep(1.5)
		self.driver.close()
		self.driver.switch_to_window(handles[0]) 
		

def main():  
	wm = Eleme('13913714891')
	wm.run()
  
if __name__ == "__main__":  
	main()  
