import scrapy


# class QuotesSpider(scrapy.Spider):
#     name = "quotes"
#
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)


# 提取数据
#
# 我们之前只是保存了HTML页面，并没有提取数据。现在升级一下代码，把提取功能加进去。至于如何使用浏览器的开发者模式分析网页，之前已经介绍过了。

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
            }


"""
网页html代码:
<div class="quote" itemscope="" itemtype="http://schema.org/CreativeWork">
    <span class="text" itemprop="text">“It is our choices, Harry, that show what we truly are, far more than our abilities.”</span>
    <span>by <small class="author" itemprop="author">J.K. Rowling</small>
        <a href="/author/J-K-Rowling">(about)</a>
        </span>
    <div class="tags">
        Tags:
        <meta class="keywords" itemprop="keywords" content="abilities,choices">

        <a class="tag" href="/tag/abilities/page/1/">abilities</a>

        <a class="tag" href="/tag/choices/page/1/">choices</a>

    </div>
</div>
"""

# 创建项目
#
# 在开始爬取之前，您必须创建一个新的Scrapy项目。 进入您打算存储代码的目录中，运行下列命令:
#
# scrapy startproject tutorialScrapyByLC
#
# 该命令将会创建包含下列内容的 tutorialScrapyByLC 目录:
#
#
# tutorialScrapyByLC/
#     scrapy.cfg            # 项目的配置文件
#     tutorialScrapyByLC/             # 该项目的python模块。之后您将在此加入代码
#         __init__.py
#         items.py          # 项目中的item文件
#         pipelines.py      # 项目中的pipelines文件
#         settings.py       # 项目的设置文件
#         spiders/          # 放置spider代码的目录
#             __init__.py
#
# 编写第一个爬虫
#
# Spider是用户编写用于从单个网站(或者一些网站)爬取数据的类。其包含了一个用于下载的初始URL，以及如何跟进网页中的链接以及如何分析页面中的内容的方法。
#
# 以下为我们的第一个Spider代码，保存在 tutorialScrapyByLC/spiders 目录下的 quotes_spider.py文件中
# 为了创建一个Spider，你必须继承 scrapy.Spider 类， 且定义以下三个属性:
#
# 1:name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
# 2:start_urls: 包含了Spider在启动时进行爬取的url列表。 因此，第一个被获取到的页面将是其中之一。 后续的URL则从初始的URL获取到的数据中提取。
# 3:parse() 是spider的一个方法。 被调用时，每个初始URL完成下载后生成的Response 对象将会作为唯一的参数传递给该函数。
# 该方法负责解析返回的数据(response data)，提取数据以及生成需要进一步处理的URL的 Request 对象。
#
# scrapy crawl quotes
#
# 再次运行这个爬虫，你将在日志里看到被提取出的数据：
#
# 保存爬取的数据
#
# 最简单存储爬取的数据的方式是使用 Feed exports:
#
# scrapy crawl quotes -o quotes.json
#
# 该命令将采用 JSON 格式对爬取的数据进行序列化，生成quotes.json文件
#
#
# 手把手教你写网络爬虫（4）：Scrapy入门 - Python - 伯乐在线
# http://python.jobbole.com/89122/
