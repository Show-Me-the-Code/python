from PIL import Image, ImageDraw, ImageFont
import urllib
import urllib.request
from io import BytesIO

# down load image avatar
avatar = 'https://avatars3.githubusercontent.com/u/1332618?v=3&s=460'
rsp = urllib.request.urlopen(avatar)
data = rsp.read()

fp = BytesIO()
fp.write(data)
fp.seek(0, 0)
image = Image.open(fp)
image.show()

base = image.convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255, 255, 255, 0))

# get a font
fnt = ImageFont.truetype('CALIBRI.TTF', 60)
fnt_size = fnt.getsize("4")

d = ImageDraw.Draw(txt)
d.text((image.size[0] - fnt_size[0] - 20, 20), "4", fill=(255, 0, 0, 255), font=fnt)

out = Image.alpha_composite(base, txt)

out.show()
