from PIL import Image, ImageDraw, ImageFont
import platform

if __name__ == '__main__':

    #config
    pic_path = './Sources/avatar';
    macos_font_path = '/Library/Fonts/Andale Mono.ttf';
    linux_font_path = '/usr/share/fonts/smc/Meera.ttf';
    unread_num = 5;
    color = '#ff0000'; #red

    pic = Image.open(pic_path);
    x_size = pic.size[0];
    y_size = pic.size[1];


    try:
        if 'Darwin' in platform.system():
            font = ImageFont.truetype(macos_font_path, x_size / 10);
        else:
            font = ImageFont.truetype(linux_font_path, x_size / 10);
    except BaseException:
        print 'System font path not find';

    draw = ImageDraw.Draw(pic);

    draw.text((9 * x_size / 10.0, 0), str(unread_num), font = font, fill = color);

    del draw;

    pic.save('./Sources/avatar_out', 'jpeg');

    print 'successfully handle the picture';
