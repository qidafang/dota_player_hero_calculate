import scrapy

class HeroItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    type = 'hero'

    tags = scrapy.Field()

    hp = scrapy.Field()
    mp = scrapy.Field()
    red = scrapy.Field()
    red_add = scrapy.Field()
    green = scrapy.Field()
    green_add = scrapy.Field()
    blue = scrapy.Field()
    blue_add = scrapy.Field()
    attack_min = scrapy.Field()
    attack_max = scrapy.Field()
    armor = scrapy.Field()
    range = scrapy.Field()
    view_day = scrapy.Field()
    view_night = scrapy.Field()
    speed = scrapy.Field()
    ballistic = scrapy.Field()
    excute_before = scrapy.Field()
    excute_after = scrapy.Field()
    attack_before = scrapy.Field()
    attack_after = scrapy.Field()

    dps = scrapy.Field()
    push = scrapy.Field()
    gank = scrapy.Field()
    support = scrapy.Field()
    meat = scrapy.Field()
    war = scrapy.Field()

class GoodItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    type = 'good'
