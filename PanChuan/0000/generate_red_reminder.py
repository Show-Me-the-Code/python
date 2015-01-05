from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def white_to_transparent(img):
	img = img.convert('RGBA')
	datas = img.getdata()
	newData=[]
	for item in datas:
		if item[0] == 255 and item[1] == 255 and item[2] == 255:
			newData.append((255,255,255,0))
		else:
			newData.append(item)
	img.putdata(newData)
	return img

p1_name = "github_logo.png"
p2_name = "red_reminder.png"
p1_image = Image.open(p1_name)
p2_image = Image.open(p2_name)
p2_transparent = white_to_transparent(p2_image)
p1_image.paste(p2_transparent,(0,0),p2_transparent)

usr_font = ImageFont.truetype("./yahei.TTF",32)
draw = ImageDraw.Draw(p1_image)
draw.text((152,8),u'12',font = usr_font)
p1_image.save("final.png","PNG")


