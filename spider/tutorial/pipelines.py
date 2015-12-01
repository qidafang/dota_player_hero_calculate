# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
import json
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        newname = item['name'] + '.jpg'
        print image_paths[0]
        print newname
        if(item.type == 'hero'):
            os.rename("d:/dota_heros/" + image_paths[0], "d:/dota_heros/hero/" + newname)
        else:
            os.rename("d:/dota_heros/" + image_paths[0], "d:/dota_heros/good/" + newname)
        return item



class JsonWriterPipeline(object):

    def __init__(self):
        self.heroFile = open('d:/dota_heros/heros.json', 'wb')
        self.goodFile = open('d:/dota_heros/goods.json', 'wb')
        self.heroFileContent = "["
        self.goodFileContent = "["

    def process_item(self, item, spider):
        entity = dict(item);
        del entity["image_urls"];
        del entity["images"];
        print entity["name"];
        #entity["name"]是中文，json.dumps里的参数表示不转为ascii
        line = (json.dumps(entity,ensure_ascii=False,indent=2) + ",\n");
        #写入文件
        if item.type == "hero":
            self.heroFileContent += line;
        else:
            self.goodFileContent += line;
        return item

    def close_spider(self, spider):
        self.heroFileContent = (self.heroFileContent[0 : len(self.heroFileContent)-2]) + "]";#为啥是减2呢？因为要减去一个逗号和一个换行符
        self.goodFileContent = (self.goodFileContent[0 : len(self.goodFileContent)-2]) + "]";

        self.heroFile.write(self.heroFileContent.encode("utf-8"))
        self.goodFile.write(self.goodFileContent.encode("utf-8"))
