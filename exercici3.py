import scrapy
from scrapy import Selector

class Exercici3Spider(scrapy.Spider):
    name = 'exercici3'
    allowed_domains = ['fisiquimicamente.com']
    start_urls = ['http://fisiquimicamente.com/blog/2022/01/23/ni-caos-ni-desorden.-que-es-la-entropia/']

    def parse(self, response):
        sel = Selector(response)
        elems = sel.css('.article')
        for elem in elems:
           print(elem.css('p::text').extract())
           #print(elem.css('h1::text').get())
           #print(elem.css('p::text').get())
