from PIL import Image, ImageFont, ImageDraw

text = "555"
img = Image.open("0000.png")
w_img, h_img=img.size
draw = ImageDraw.Draw(img)
font = ImageFont.truetype("msyh.ttf", 10)
w_font, h_font = draw.textsize(text, font)
draw.text((w_img-w_font, 0), text, fill="red", font=font)
img.save('0000-out.png')
