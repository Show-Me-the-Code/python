import Image,ImageFont,ImageDraw
text='6'
image = Image.open('0.jpg')
width,height=image.size
font=ImageFont.truetype('Inconsolata.otf',width/6) #set fonttype and size

draw=ImageDraw.Draw(image)
s_width,s_heitht=draw.textsize(text,font) # get text size
draw.text((width-s_width,0), text, fill=(255,0,0),font=font)
image.save('0add.jpg')
