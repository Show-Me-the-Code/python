# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log
import requests
import os

class ImageDownloadAndMongoDBPipeline(object):

    def __init__(self):
        # 创建mongodb连接
        connection = pymongo.MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        valid = True
        # 检查是否合法
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            # 定义目录地址
            dir_path = '%s/%s' % (settings['IMAGES_STORE'], spider.name)
            # 检查目录是否存在
            if not os.path.exists(dir_path):
                log.msg("不存在目录，创建",
                        level=log.DEBUG, spider=spider)
                os.makedirs(dir_path)

            image_url = item['Img_url']
            # 文件名
            us = image_url.split('/')[3:]
            image_file_name = '_'.join(us)
            file_path = '%s/%s' % (dir_path, image_file_name)

            if not os.path.exists(file_path):
                # 检查是否已经下载过 若不存在 下载该图片
                with open(file_path, 'wb') as handle:
                    response = requests.get(image_url, stream=True)
                    for block in response.iter_content(1024):
                        if block:
                            handle.write(block)

                item['File_path'] = file_path
                log.msg("已下载图片!",
                        level=log.DEBUG, spider=spider)

                # 数据库记录
                self.collection.insert(dict(item))
                log.msg("已存入数据库!",
                        level=log.DEBUG, spider=spider)
            else:
                log.msg("已下载过该图片，跳过",
                        level=log.DEBUG, spider=spider)


        return item
