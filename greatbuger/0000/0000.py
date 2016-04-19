'''from PIL import Image,ImageFont,ImageDraw

class UnreadTag:
    def __init__(self):
        self.img = None
        self.num = None
        
    def open(self,image_path):
        self.img = Image.open(image_path)
        return True
        
    def draw(self,tag_num = 1):
        tag_size = max(self.img.size[0],self.img.size[1]) / 5
        tag_str = str(tag_num) if tag_num < 100 else '99+'
        font = ImageFont.truetype("simsun.ttc",tag_size)
        px = self.img.size[0]-font.getsize(tag_str)[0]
        draw_pen = ImageDraw.Draw(self.img)
        draw_pen.text((px,0), tag_str, (255,0,0), font)
        self.img.save('D:/python workSpace/showmethecode/0000/face' + tag_str + '.jpg')
        return True
        
        
solver = UnreadTag()
solver.open('D:/python workSpace/showmethecode/0000/face.jpg')
solver.draw(25)
'''


from PIL import Image,ImageDraw,ImageFont

class UnreadInformation:
    def __init__(self):
        self.image = None
        self.unread = None
    
    def open(self,image_path):
        self.image = Image.open(image_path)
        return True
        
    def draw(self,unread = 1):
        unread_str = str(unread) if unread < 100 else '99+'
        unread_size = max(self.image.size[0],self.image.size[1]) / 4
        font = ImageFont.truetype("simsun.ttc",unread_size)
        location_x = (self.image.size[0] - font.getsize(unread_str)[0])
     
        draw = ImageDraw.Draw(self.image)
        draw.text((location_x,0),unread_str,(255,0,0),font)
        
        self.image.save('D:/python workSpace/showmethecode/0000/face' + unread_str + '.jpg')
        return True

test = UnreadInformation()
test.open('D:/python workSpace/showmethecode/0000/face.jpg')
test.draw(25)

        
        

        
        
    


























        
        
        
        
        
