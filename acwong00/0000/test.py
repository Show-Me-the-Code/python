from PIL import Image, ImageDraw, ImageFont

original = Image.open("acwong.jpg")

fnt = ImageFont.truetype("msyh.ttf", 80)

d = ImageDraw.Draw(original)

d.text((200, 0), "6", font=fnt, fill=(255,0,0,255))

original.save("finnal.jpg")
