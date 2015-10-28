# -*- coding: utf-8 -*-

# Scrapy settings for baidutieba project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'baidutieba'

SPIDER_MODULES = ['baidutieba.spiders']
NEWSPIDER_MODULE = 'baidutieba.spiders'

ITEM_PIPELINES = {'baidutieba.pipelines.ImageDownloadAndMongoDBPipeline': 1}
# 存放图片路径
IMAGES_STORE = '/home/bill/Pictures'

# mongodb配置
MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "meizidb"
MONGODB_COLLECTION = "meizi"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'baidutieba (+http://www.yourdomain.com)'
