# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import Selector
from practice13.items import Practice13Item

class TiebapicSpider(scrapy.Spider):
    name = "shan"
    allowed_domains = ["tieba.baidu.com"]
    start_urls = ['http://tieba.baidu.com/p/2166231880']

    def parse(self,response):
        sel = Selector(response)
        div1 = sel.xpath('.//div[@class="d_post_content j_d_post_content  clearfix"]')
        #print div1
        for single1 in div1:
            div2 = single1.xpath('./img')
            #print div2
            for single2 in div2:
                item = Practice13Item()
                item['image_urls'] = [single2.xpath('./@src').extract()[0]]
                print item['image_urls']
                yield item
