# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Meijunew100ScrapybylcPipeline(object):
    def process_item(self, item, spider):
        # 先将内容写入my_meiju.txt
        with open("my_meiju.txt", 'a', encoding='utf-8') as fp:
            fp.write(item['name'] + '-' + item['movieUrl'] + '\n')

        # 打印输出一下
        print(item['name'] + '-' + item['movieUrl'] + '\n')

        # 再return item
        # 这样的话命令>scrapy crawl meiju -o my_meiju.json也可以用了，不报错.
        return item
