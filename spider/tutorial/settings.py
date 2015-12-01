# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['tutorial.spiders']
NEWSPIDER_MODULE = 'tutorial.spiders'

ITEM_PIPELINES = {
    'tutorial.pipelines.MyImagesPipeline': 1,
    'tutorial.pipelines.JsonWriterPipeline': 800,
    'scrapy.contrib.pipeline.images.ImagesPipeline': 500
}
IMAGES_STORE = 'd:/dota_heros/'

FEED_URI = 'd:/dota_heros.json'
FEED_FORMAT = 'JSON'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
