#coding=utf-8
from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt

#读取停用词
stopwords={}
def stopword(filename=''):
	global stopwords	#函数外全局变量
	f=open(filename,'r')
	line=f.readline().rstrip()#rstrip()删除末尾指定字符
	while line:
		stopwords.setdefault(line,0)
		stopwords[line.decode('utf-8')]=1
		line=f.readline().rstrip()
	f.close()
	stopword(filename='/home/joezhu/Python/百度贴吧.txt')

#定义中文分词和停用词清洗
def cleancntxt(txt,stopwords):
	seg_generator=jieba.cut(txt,cut_all=False)
	seg_list=[i for i in seg_generator if i not in stopwords]
	seg_list=[i for i in seg_list if i!=u'']
	return(seg_list)

#定义中文词云函数
def wordcloudplot(txt):
	wordcloud=WordCloud(font_path='/usr/share/matplotlib/mpl-data/fonts/ttf/msyh.ttf',background_color="black",margin=5,width=1800,height=800)#背景颜色可以选black或white,长宽度控制清晰程度
	wordcloud=wordcloud.generate(txt)
	#open a plot of the generated image.
	plt.imshow(wordcloud)
	plt.axis("off")
	plt.show()

def plotTitleCloud(txtlist):
    	txt=r' '.join(txtlist)
    	seg_list=cleancntxt(txt, stopwords)
    	#seg_list = jieba.cut(txt, cut_all=False)
    	txt=r' '.join(seg_list)
    	wordcloudplot(txt)

with open('/home/joezhu/Python/百度贴吧.txt') as f:
	t1=f.readlines()
	plotTitleCloud(t1)



	

	
