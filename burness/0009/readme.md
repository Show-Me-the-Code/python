0009-如何找出html中的链接
======

### HTMLParser库

	* handle_starttage(tag, attrs)
	* handle_startendtage(tag, attrs)
	* handle_endtage(tag)

更改上述函数来实现自己需要的功能

	* tag是html标签，
	* attrs是(属性，值)元组的list
	* HTMLParser自动将tag和attrs都转为小写

    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        if tag == "a":
            if len(attrs) == 0: pass
            else:
                for (variable, value)  in attrs:
                    if variable == "href":
                        self.links.append(value)