# -*- coding: utf-8 -*-

import scrapy
from tutorial.items import HeroItem
from tutorial.items import GoodItem

import re

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["db.dota.uuu9.com"]
    start_urls = [
        "http://db.dota.uuu9.com/"
    ]
    hero_items = {}

    def parse(self, response):
        for link in response.css("#herodata a"):
            item = HeroItem();
            item['id'] = link.css("img::attr(hid)").extract()[0];
            item['name'] = link.css("span::text").extract()[0];
            item['image_urls'] = link.css("img::attr(src)").extract();
            url = link.css("::attr(href)").extract()[0];
            self.hero_items["http://db.dota.uuu9.com" + url] = item;
            yield scrapy.Request("http://db.dota.uuu9.com" + url, callback=self.parseHero)
        for link2 in response.css("#goodslist1 a"):
            item2 = GoodItem();
            item2['id'] = link2.css("img::attr(gid)").extract()[0];
            item2['name'] = link2.css("span::text").extract()[0];
            item2['image_urls'] = link2.css("img::attr(src)").extract();
            yield item2

    def parseHero(self, response):
        item = self.hero_items[response.url];

        tags = response.css(".tag>a::text").extract();
        tagsStr = "";
        for t in tags:
            tagsStr += (t + ",");
        item['tags'] = tagsStr[0 : len(tagsStr) - 1];

        lis = response.css(".ponent>li");
        index = 0;
        for li in lis:
            name = li.css("em::text").extract()[0].encode("gb2312").strip();
            value = li.css("b::text").extract()[0].encode("gb2312").strip();
            val = float(value);
            if index == 0:
                item['dps'] = val;
            elif index == 1:
                item['push'] = val;
            elif index == 2:
                item['gank'] = val;
            elif index == 3:
                item['support'] = val;
            elif index == 4:
                item['meat'] = val;
            elif index == 5:
                item['war'] = val;
            index += 1;

        spans = response.css(".pageright>.bord>.bute>.jianbg>span");
        for s in spans:
            name = s.css("label::text").extract()[0].encode("gb2312").strip();
            texts = s.css("::text").extract();
            value = texts[len(texts) - 1].encode("gb2312").strip();
            ptn = re.compile("([\d|\.]+)[\D]*([\d|\.]+).*");#正则，两个数字
            if name == '生命'.decode("utf-8").encode("gb2312"):
                item['hp'] = int(value);
            elif name == '魔法'.decode("utf-8").encode("gb2312"):
                item['mp'] = int(value);
            elif name == '力量'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['red'] = int(m.group(1));
                item['red_add'] = float(m.group(2));
            elif name == '敏捷'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['green'] = int(m.group(1));
                item['green_add'] = float(m.group(2));
            elif name == '智力'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['blue'] = int(m.group(1));
                item['blue_add'] = float(m.group(2));
            elif name == '初始攻击'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['attack_min'] = int(m.group(1));
                item['attack_max'] = int(m.group(2));
            elif name == '初始护甲'.decode("utf-8").encode("gb2312"):
                item['armor'] = float(value);
            elif name == '攻击范围'.decode("utf-8").encode("gb2312"):
                item['range'] = int(value);
            elif name == '视野（白天/黑夜）'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['view_day'] = int(m.group(1));
                item['view_night'] = int(m.group(2));
            elif name == '移动速度'.decode("utf-8").encode("gb2312"):
                item['speed'] = int(value);
            elif name == '弹道速度'.decode("utf-8").encode("gb2312"):
                item['ballistic'] = int(value);
            elif name == '施法前摇/后摇'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['excute_before'] = float(m.group(1));
                item['excute_after'] = float(m.group(2));
            elif name == '攻击前摇/后摇'.decode("utf-8").encode("gb2312"):
                m = ptn.match(value);
                item['attack_before'] = float(m.group(1));
                item['attack_after'] = float(m.group(2));
        yield item
            


