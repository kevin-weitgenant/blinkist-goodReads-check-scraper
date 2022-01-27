import scrapy


class GoodreadsSpider(scrapy.Spider):
    name = 'GoodReads'
    allowed_domains = ['goodreads.com']
    start_urls = ['https://www.goodreads.com/review/list/109133436-kevin-weitgenant?page=1&shelf=to-read']

    def parse(self, response):
        
        next_page = response.xpath("//a[@class = 'next_page']/@href").get()

        titulos = []
        urls = []
        for titulo in response.xpath('//tr[@class = "bookalike review"]'):       
            titulos.append(titulo.xpath('.//td[@class= "field title"]/div/a/@title').get())
            urls.append(titulo.xpath('.//td[@class= "field title"]/div/a/@href').get())
        urls = ["www.goodreads.com" + x for x in urls]

        dictionary = {titulos[i]:urls[i] for i in range(len(titulos))}
     
        if next_page:
            yield response.follow(url=next_page, callback=self.parse)

        yield {
            "urls": dictionary
        }
        
        
    #     yield response.follow(url = urls[0], callback = self.parse_check_otherEditions, meta = [titulos,urls]  )

    # def parse_check_otherEditions(self,response):
    #     if response.xpath('//div[@class = "coverButton" and contains(a,"Other editions")]/a/@href'):
    #         pass


    # def parse_otherEditions(self,response):
    #     pass