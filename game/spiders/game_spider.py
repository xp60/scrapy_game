import scrapy
from game.items import GameItem

class GameSpider(scrapy.Spider):
    name = 'game'
    start_urls = [
        'http://www.4399.com/',
    ]

    def parse(self, response):
        for quote in response.xpath('//ul/li/a'):
            yield {
                'name': quote.xpath('text()').extract(),
                'link': quote.xpath('@href').extract()
            }
        next_page_url = response.xpath('//ul/li/a/@href').extract()[10]
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

