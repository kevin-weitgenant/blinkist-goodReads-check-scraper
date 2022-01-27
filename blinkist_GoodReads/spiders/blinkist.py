import scrapy


class BlinkistSpider(scrapy.Spider):
    name = 'blinkist'
    allowed_domains = ['blinkist.com']
    start_urls = ['https://www.blinkist.com/sitemap/']

    def parse(self, response):
        


        
        pass
