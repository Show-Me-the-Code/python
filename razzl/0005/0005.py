'''
It can resize the photos in a file
'''

import os
from PIL import Image

def resize_photo(source_dir,width,higth,destination_dir):
	photos = os.listdir(source_dir)
	for photo in photos:
		photo_abspath = os.path.join(source_dir,photo)#if you use os.path.abspath,there may be some error
		print photo_abspath
		if(os.path.isfile(photo_abspath)):#os.path.isfile need a abspath
			im = Image.open(photo_abspath)
			#w,h = im.size
			new_im = im.resize((width,higth))#note: the resize returns a resized copy of an image , so you need a new object to save it 
			destination_path = os.path.join(destination_dir,photo)
			new_im.save(destination_path)
			print destination_path
resize_photo('C:/Users/razzl/Desktop/1',800,800,'C:/Users/razzl/Desktop/2')


