# coding =utf-8
from goose import Goose
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#config
HTMLPATH = 'http://www.chinadaily.com.cn/a/201802/11/WS5a7f7e29a3106e7dcc13bf6b.html'

if __name__ == '__main__':
    g = Goose();
    page = g.extract(HTMLPATH);
    print page.cleaned_text;
