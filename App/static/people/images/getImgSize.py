#encoding=utf-8
#缩放图片
#use:
#cmd中输入命令
#python getImgSize.py 1.jpg one.jpg 54 54

import os
import sys
from PIL import Image

def processIcon(newName,filename,ary):
	#打开文件
	img = Image.open(filename).convert("RGBA")
	#尺寸缩放
	im = img.resize((ary[0],ary[1]),Image.BILINEAR)
	#保存图片
	im.save(newName)
	print 'Congratulations!It\'s all done!'

if __name__ == ("__main__"):
	#取得参数
	filename = sys.argv[1]
	newName = sys.argv[2]
	sizeW = sys.argv[3]
	siezH = sys.argv[4]
	if not os.path.exists(filename):
		print 'Hey,File Not Found!'
	else:
		processIcon(newName,filename,[int(sizeW),int(siezH)])
