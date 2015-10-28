# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from baidutieba.items import BaidutiebaItem
from scrapy.selector import Selector
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class MeiziSpider(CrawlSpider):
    name = "meizi"
    allowed_domains = ["baidu.com"]
    print "开始爬取妹子图"
    start_urls = (
        'http://tieba.baidu.com/p/2166231880',
    )

    # 定义parse方法，用来解析
    def parse(self, response):
        # 找出所有类为BDE_Image的图片
        AllImg = Selector(response).xpath('//img[@class="BDE_Image"]')
        for img in AllImg:
            item = BaidutiebaItem()
            item['Img_name'] = img.xpath('@bdwater').extract()[0]
            item['Img_url'] = img.xpath('@src').extract()[0]
            yield item
