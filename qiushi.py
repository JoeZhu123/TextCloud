__author__='Joe'
#._*_ coding:utf-8 _*_
import urllib
import urllib2
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')



#糗事百科爬虫类
class QSBK:
	#初始化方法，定义一些变量
	def __init__(self):
		self.page=input
		self.user_agent='Mozilla/4.0 (compatible;MSIE 5.5;Windows NT)'
		#初始化headers
		self.headers={'User-Agent':self.user_agent}
		#存放程序是否继续运行的标志
		self.enable=False
	#传入某一页的索引，获得页面代码
	def getPage(self,pageIndex):
		try:
			url='http://www.qiushibaike.com/hot/page/'+str(pageIndex)
			request=urllib2.Request(url,headers=self.headers)
			response=urllib2.urlopen(request)
		#	print response.read()
			content=response.read().decode('utf-8')
			return content
		except urllib2.URLError,e:
			if hasattr(e,"code"):
				print u"错误代码",e.code
			if hasattr(e,"reason"):
				print u"连接糗事百科失败，错误原因",e.reason
			return None
	#加载并提取页面的内容
	def getPageItems(self,pageIndex):
		content=self.getPage(pageIndex)
		if not content:
			print "页面加载失败...."
			return None
		pattern=re.compile('<div class="content">(.*?)</div>',re.S)
	#	pattern=re.compile('<i class="number">(.*?)</i>',re.S)
		items=re.findall(pattern,content)
	#	haveImg=re.search("img",item[3])
	#	if haveImg:
		return items
	#将爬取的内容保存到txt中
	def savePage(self,items):
		f = open("test1.txt","w+")		
		for item in items:
			print item.decode('utf-8')	
			f.write(item.decode('utf-8'))
		f.close()
		return
	#开始方法
	def start(self):
		print u"正在读取糗事百科，按回车输入页面数，输出页面段子并保存，Q退出"
		#使变量为true，程序持续运行
		self.enable=True
		#用来存储每页的段子
		pageStories=[]	
		while self.enable:				
			#等待输入页面数		
			input=raw_input()
			if input=="Q":
				self.enable=False
				return
			print u"糗事百科热门第%d页" %(int(input))
			#加载页面
			pageStories=self.getPageItems(int(input))
			#打印并保存段子
			self.savePage(pageStories)

spider=QSBK()
spider.start()
